#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path
import shutil

EOI = b"\xff\xd9"  # JPEG End Of Image marker

XMP_OPEN = b"<x:xmpmeta"
XMP_CLOSE = b"</x:xmpmeta>"

# --- XMP helpers --------------------------------------------------------------

def extract_xmp(blob: bytes) -> str | None:
    """Return the first XMP packet as a UTF-8 string, or None if not found."""
    start = blob.find(XMP_OPEN)
    if start == -1:
        return None
    end = blob.find(XMP_CLOSE, start)
    if end == -1:
        return None
    end += len(XMP_CLOSE)
    try:
        return blob[start:end].decode("utf-8", errors="replace")
    except Exception:
        return None

def xmp_find_microvideo_offset(xmp: str) -> int | None:
    """
    Older Pixels: <GCamera:MicroVideoOffset>12345</GCamera:MicroVideoOffset>
    Offset is the number of bytes from the start of the MP4 to EOF (i.e., MP4 length).
    """
    m = re.search(r"<[^:>]*:?MicroVideoOffset>(\d+)</", xmp, flags=re.I)
    if m:
        return int(m.group(1))
    return None

def xmp_find_gcontainer_video_length_and_padding(xmp: str) -> tuple[int, int] | None:
    """
    Newer Pixels (Motion Photo V1): a <...Container:Directory> with items.
    We look for the item whose mime contains video/mp4 and read its Length and Padding.
    Returns (video_length, video_padding) or None.
    Works with both 'GContainer' and 'Container' namespaces, and both ItemMime/ItemLength
    vs Item:Mime/Item:Length spellings.
    """
    # Normalize whitespace for easier regex
    x = " ".join(xmp.split())

    # Try attribute variants (ItemMime/ItemLength/ItemPadding) or (Item:Mime/Item:Length/Item:Padding)
    # and allow Container or GContainer namespaces.
    pattern = (
        r"<(?:[A-Za-z]*Container):Item[^>]*?"
        r'(?:ItemMime|Item:Mime)\s*=\s*"video/mp4"[^>]*?'
        r'(?:ItemLength|Item:Length)\s*=\s*"(\d+)"[^>]*?'
        r'(?:ItemPadding|Item:Padding)\s*=\s*"(\d+)"'
    )
    m = re.search(pattern, x, flags=re.I)
    if m:
        length = int(m.group(1))
        padding = int(m.group(2))
        return (length, padding)

    # If padding wasn't stored, try without it (assume 0)
    pattern_no_pad = (
        r"<(?:[A-Za-z]*Container):Item[^>]*?"
        r'(?:ItemMime|Item:Mime)\s*=\s*"video/mp4"[^>]*?'
        r'(?:ItemLength|Item:Length)\s*=\s*"(\d+)"'
    )
    m2 = re.search(pattern_no_pad, x, flags=re.I)
    if m2:
        return (int(m2.group(1)), 0)

    return None

# --- Core carve logic ---------------------------------------------------------

def split_motion_photo(data: bytes) -> tuple[bytes, bytes | None]:
    """
    Split a Google Motion Photo into (still_jpeg_bytes, video_mp4_bytes_or_None).
    Strategy:
      1) Use XMP MicroVideoOffset (old) or GContainer/Container ItemLength (new).
      2) Fallback: cut at the last JPEG EOI marker.
    """
    file_size = len(data)
    xmp = extract_xmp(data)

    # 1a) MicroVideoOffset (older format)
    if xmp:
        offset = xmp_find_microvideo_offset(xmp)
        if offset and offset > 0 and offset < file_size:
            video_len = offset
            video_start = file_size - video_len
            still = data[:video_start]
            video = data[video_start:video_start + video_len]
            # Ensure still ends with EOI; if not, fallback to rfind below
            if still.endswith(EOI):
                return still, video

        # 1b) Newer GContainer/Container format: use ItemLength (+Padding)
        vp = xmp_find_gcontainer_video_length_and_padding(xmp)
        if vp:
            video_len, video_pad = vp
            tail = video_len + max(0, video_pad)
            if 0 < tail <= file_size:
                video_start = file_size - tail
                video_end = video_start + video_len
                still = data[:video_start]
                video = data[video_start:video_end]
                if still.endswith(EOI):
                    return still, video

    # 2) Fallback: cut at the last EOI (handles cases with embedded thumbnails)
    last_eoi = data.rfind(EOI)
    if last_eoi == -1:
        # Not a JPEG or severely malformed
        return data, None

    still = data[: last_eoi + 2]
    remainder = data[last_eoi + 2 :]
    # If remainder looks like MP4 (contains 'ftyp' header), keep it; else, drop.
    # This is a light heuristic for nicer logs.
    if b"ftyp" in remainder[:64]:
        return still, remainder
    return still, None

# --- Batch processing ---------------------------------------------------------

def process_file(src: Path, dst_img: Path, dst_vid: Path | None, keep_video: bool) -> None:
    with src.open("rb") as f:
        data = f.read()

    still, video = split_motion_photo(data)
    dst_img.parent.mkdir(parents=True, exist_ok=True)
    with dst_img.open("wb") as f:
        f.write(still)
    shutil.copystat(src, dst_img, follow_symlinks=False)

    if keep_video and video:
        assert dst_vid is not None
        dst_vid.parent.mkdir(parents=True, exist_ok=True)
        with dst_vid.open("wb") as f:
            f.write(video)
        shutil.copystat(src, dst_vid, follow_symlinks=False)

def iter_images(root: Path):
    exts = {".jpg", ".jpeg", ".mp.jpg", ".mp.jpeg"}
    for p in root.rglob("*"):
        if p.is_file() and any(str(p).lower().endswith(ext) for ext in exts):
            yield p

def main():
    ap = argparse.ArgumentParser(
        description="Strip Google Pixel Motion Photo video from .jpg/.mp.jpg files."
    )
    ap.add_argument("input", help="Input file or directory")
    ap.add_argument("output", help="Output directory")
    ap.add_argument("--extract-video", action="store_true", help="Also save motion video as .mp4")
    ap.add_argument("--mirror", action="store_true", help="Mirror input subfolders under output")
    ap.add_argument("--flat", action="store_true", help="Put all results directly in output (no mirroring)")
    args = ap.parse_args()

    in_path = Path(args.input)
    out_root = Path(args.output)
    out_root.mkdir(parents=True, exist_ok=True)

    paths = []
    if in_path.is_file():
        paths = [in_path]
    else:
        paths = list(iter_images(in_path))

    if not paths:
        print("No matching JPEG files found.")
        return

    for src in paths:
        # Determine relative output path
        if args.flat and in_path.is_dir():
            rel = src.name
        elif args.mirror and in_path.is_dir():
            rel = src.relative_to(in_path)
        else:
            # default: keep just the filename when input is a dir; mirror when a single file
            rel = src.name if in_path.is_dir() else src.name

        rel = Path(rel)
        stem = rel.name
        # Remove .mp part if present
        if stem.lower().endswith(".mp.jpg"):
            out_stem = stem[:-7]  # strip ".mp.jpg"
        elif stem.lower().endswith(".mp.jpeg"):
            out_stem = stem[:-8]
        else:
            out_stem = Path(stem).stem

        dst_dir = out_root / (rel.parent if (args.mirror and in_path.is_dir()) else Path())
        dst_img = dst_dir / f"{out_stem}.jpg"
        dst_vid = dst_dir / f"{out_stem}.mp4" if args.extract_video else None

        try:
            process_file(src, dst_img, dst_vid, args.extract_video)
            msg = f"Saved still: {dst_img}"
            if args.extract_video and dst_vid and dst_vid.exists():
                msg += f" | video: {dst_vid}"
            print(msg)
        except Exception as e:
            print(f"FAILED {src}: {e}")

if __name__ == "__main__":
    main()
