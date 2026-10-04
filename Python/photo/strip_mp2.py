#!/usr/bin/env python3
"""
pixel7_strip_motion.py

Strip Motion Photo video from Pixel 7 .mp.jpg/.MP.jpg files.

Usage examples:
  # Process directory, mirror subfolders, and extract videos:
  python pixel7_strip_motion.py /path/to/in /path/to/out --extract-video --mirror

  # Process directory flat (no subfolders)
  python pixel7_strip_motion.py /path/to/in /path/to/out --extract-video --flat
"""
from pathlib import Path
import argparse
import re
import shutil

EOI = b"\xff\xd9"  # JPEG End Of Image marker

def extract_xmp_block(data: bytes) -> bytes | None:
    """Return the raw XMP packet bytes if present, else None."""
    start = data.find(b"<x:xmpmeta")
    if start == -1:
        return None
    end = data.find(b"</x:xmpmeta>", start)
    if end == -1:
        return None
    end += len(b"</x:xmpmeta>")
    return data[start:end]

def parse_container_items(xmp: bytes):
    """
    Parse XMP for Container/GContainer <Item> entries.
    Returns a list of dicts with keys: mime (str), length (int|None), padding (int|0)
    Supports both attribute-style and child-element style.
    """
    x = xmp.decode("utf-8", errors="replace")
    items = []

    # 1) Attribute-style opening tags:
    #   <Container:Item ItemMime="video/mp4" ItemLength="12345" ItemPadding="0" ... />
    for m in re.finditer(r'<(?:[A-Za-z0-9_-]+:)?Item\b([^>]*)>', x, flags=re.IGNORECASE):
        attr_text = m.group(1)
        if not attr_text:
            continue
        attrs = dict(re.findall(r'([A-Za-z0-9_:.-]+)\s*=\s*"([^"]*)"', attr_text))
        # Normalize keys by removing namespace prefix if present
        norm = {k.split(":")[-1]: v for k, v in attrs.items()}
        mime = norm.get("ItemMime") or norm.get("Mime") or norm.get("itemmime")
        if mime:
            length = norm.get("ItemLength") or norm.get("Length") or norm.get("itemlength")
            padding = norm.get("ItemPadding") or norm.get("Padding") or norm.get("itempadding")
            try:
                length = int(length) if length is not None else None
            except Exception:
                length = None
            try:
                padding = int(padding) if padding is not None else 0
            except Exception:
                padding = 0
            items.append({"mime": mime, "length": length, "padding": padding})

    # 2) Child-element style:
    #   <Container:Item> <Container:ItemMime>video/mp4</Container:ItemMime>
    #                   <Container:ItemLength>12345</Container:ItemLength> ... </Container:Item>
    for m in re.finditer(r'<(?:[A-Za-z0-9_-]+:)?Item\b[^>]*>(.*?)</(?:[A-Za-z0-9_-]+:)?Item>', x, flags=re.DOTALL|re.IGNORECASE):
        inner = m.group(1)
        def tag_val(name_variants):
            for name in name_variants:
                regex = r'<(?:[A-Za-z0-9_-]+:)?' + re.escape(name) + r'>([^<]+)</'
                mm = re.search(regex, inner, flags=re.IGNORECASE)
                if mm:
                    return mm.group(1).strip()
            return None

        mime = tag_val(["ItemMime", "Mime", "Item:Mime"])
        length = tag_val(["ItemLength", "Length", "Item:Length"])
        padding = tag_val(["ItemPadding", "Padding", "Item:Padding"])
        try:
            length = int(length) if length is not None else None
        except Exception:
            length = None
        try:
            padding = int(padding) if padding is not None else 0
        except Exception:
            padding = 0
        if mime:
            items.append({"mime": mime, "length": length, "padding": padding})

    return items

def find_ftyp_based_video(data: bytes, min_start_search: int = 0):
    """
    Heuristic fallback: look for 'ftyp' occurrences after min_start_search,
    try to recover mp4 by inspecting the 4 byte size before 'ftyp'.
    Returns tuple (still_end_index, video_bytes) or (None, None) if not found.
    """
    idx = data.find(b'ftyp', min_start_search)
    candidates = []
    while idx != -1:
        candidates.append(idx)
        idx = data.find(b'ftyp', idx + 1)

    # try candidates from earliest after min_start_search to last
    for pos in candidates:
        start = pos - 4
        if start < 0:
            continue
        # read box size (big-endian)
        try:
            size = int.from_bytes(data[start:start+4], 'big')
        except Exception:
            size = 0
        # If size is 0 (means box extends to EOF per spec), accept as candidate
        candidate_video = None
        if size == 0:
            candidate_video = data[start:]
        elif size == 1:
            # 64-bit size: next 8 bytes contain size (rare). We'll accept from start to EOF.
            candidate_video = data[start:]
        else:
            # if size looks sane, use it; otherwise fallback to taking everything from start
            if size >= 8 and (start + size) <= len(data):
                candidate_video = data[start:start+size] + data[start+size:]
            else:
                candidate_video = data[start:]

        # sanity check: candidate_video should contain 'ftyp' near the beginning
        if candidate_video and b'ftyp' in candidate_video[:64]:
            # find last EOI before this start
            last_eoi = data.rfind(EOI, 0, start)
            if last_eoi != -1 and last_eoi + 2 <= start:
                return last_eoi + 2, candidate_video
            else:
                # as a fallback allow still to be everything before start
                return start, candidate_video

    return None, None

def split_motion_photo(data: bytes):
    """Return (still_bytes, video_bytes_or_None)."""
    file_size = len(data)
    # 1) Try XMP Container parse
    xmp = extract_xmp_block(data)
    if xmp:
        items = parse_container_items(xmp)
        # find item with video/mp4 mime (case-insensitive substring)
        for it in items:
            if it.get("mime") and "video" in it["mime"].lower():
                length = it.get("length")
                padding = it.get("padding") or 0
                if length and length > 0 and length + padding <= file_size:
                    tail = length + padding
                    video_start = file_size - tail
                    # find the last EOI before video_start (to avoid embedded thumbnails)
                    last_eoi = data.rfind(EOI, 0, video_start)
                    if last_eoi != -1:
                        still = data[: last_eoi + 2]
                    else:
                        # As a fallback, use bytes up to video_start
                        still = data[: video_start]
                    video = data[video_start: video_start + length]
                    # sanity check: video should contain 'ftyp' near its start
                    if b"ftyp" in video[:64]:
                        return still, video
                    # if not, continue to other heuristics below
    # 2) Heuristic: find 'ftyp' after last EOI (or after half the file)
    last_eoi_global = data.rfind(EOI)
    search_start = (last_eoi_global + 2) if last_eoi_global != -1 else max(0, file_size // 2)
    still_end, video = find_ftyp_based_video(data, min_start_search=search_start)
    if video:
        still = data[: still_end] if still_end is not None else data[:data.rfind(EOI) + 2 if data.rfind(EOI) != -1 else 0]
        # ensure still ends with EOI; if not, find last EOI before video start
        if not still.endswith(EOI):
            le = data.rfind(EOI, 0, len(still))
            if le != -1:
                still = data[: le + 2]
        return still, video

    # 3) Last-resort: cut at last EOI; this yields a still but video may be ignored
    last_eoi = data.rfind(EOI)
    if last_eoi != -1:
        still = data[: last_eoi + 2]
        remainder = data[last_eoi + 2 :]
        if b"ftyp" in remainder[:256]:
            # assume remainder is mp4
            return still, remainder
        # no usable video found
        return still, None

    # if no EOI found at all, return whole file as still and no video
    return data, None

def process_file(src: Path, dst_img: Path, dst_vid: Path | None, keep_video: bool):
    b = src.read_bytes()
    still, video = split_motion_photo(b)
    dst_img.parent.mkdir(parents=True, exist_ok=True)
    dst_img.write_bytes(still)
    try:
        shutil.copystat(src, dst_img)
    except Exception:
        pass
    print(f"Saved still: {dst_img} (size {len(still)} bytes)")

    if keep_video:
        if video:
            assert dst_vid is not None
            dst_vid.parent.mkdir(parents=True, exist_ok=True)
            dst_vid.write_bytes(video)
            try:
                shutil.copystat(src, dst_vid)
            except Exception:
                pass
            print(f" Extracted video: {dst_vid} (size {len(video)} bytes)")
        else:
            print(" No video found for this file.")

def iter_images(root: Path):
    extensions = {".jpg", ".jpeg", ".mp.jpg", ".mp.jpeg", ".mpjpg"}
    for p in root.rglob("*"):
        if p.is_file() and any(str(p).lower().endswith(ext) for ext in extensions):
            yield p

def main():
    ap = argparse.ArgumentParser(description="Strip Pixel Motion Photo (Pixel 7 compatible).")
    ap.add_argument("input", help="Input file or directory")
    ap.add_argument("output", help="Output directory")
    ap.add_argument("--extract-video", action="store_true", help="Also save motion video as .mp4")
    ap.add_argument("--mirror", action="store_true", help="Mirror input subfolders under output")
    ap.add_argument("--flat", action="store_true", help="Put all results directly in output (no mirroring)")
    args = ap.parse_args()

    in_path = Path(args.input)
    out_root = Path(args.output)
    out_root.mkdir(parents=True, exist_ok=True)

    paths = [in_path] if in_path.is_file() else list(iter_images(in_path))
    if not paths:
        print("No matching files found.")
        return

    for src in paths:
        if in_path.is_dir():
            if args.flat:
                out_sub = out_root
            elif args.mirror:
                try:
                    rel = src.relative_to(in_path).parent
                except Exception:
                    rel = Path()
                out_sub = out_root / rel
            else:
                out_sub = out_root
        else:
            out_sub = out_root

        stem = src.name
        # normalize name: remove trailing .mp before jpg if present
        if stem.lower().endswith(".mp.jpg"):
            out_stem = stem[:-7]
        elif stem.lower().endswith(".mp.jpeg"):
            out_stem = stem[:-8]
        else:
            out_stem = Path(stem).stem

        dst_img = out_sub / f"{out_stem}.jpg"
        dst_vid = out_sub / f"{out_stem}.mp4" if args.extract_video else None

        try:
            process_file(src, dst_img, dst_vid, args.extract_video)
        except Exception as e:
            print(f"FAILED {src}: {e}")

if __name__ == "__main__":
    main()
