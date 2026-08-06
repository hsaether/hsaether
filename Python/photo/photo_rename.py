import argparse
import json
import os
from datetime import datetime, timezone
import ffmpeg

import photo_suport as photo_sup

'''
Not all files has meta information about camera.
Not all have timezone information
GPS is not used for timezone
InfoTag means camera from Meta
InfoDate means date from meta
'''

PIC_EXT = ["jpeg", "jpg", 'dng', "heic", 'png', 'tiff', 'tif', 'crw', 'cr2', 'cr3', 'arw', 'nef']
VID_EXT = ["mp4", "avi", 'mov']
IGN_EXT = ["thm", "info", "json", "pdf", "xls", "xlsx", "doc", "docx", "wks", "htm", "ini", "gif", "wdb", "x3d", "ppt"]


def format_record_date(dt) -> str | None:
    if dt is None:
        return None
    return dt.isoformat(timespec='microseconds')


def build_plan(path: str, info: bool = True):
    rec_list = []
    rename_list = []

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            probe = None
            camera = 'Unknown'
            model = "Unknown"
            ext_tag = 'ooo'
            info_tag = False
            info_date = False
            dt = None

            file = os.path.abspath(os.path.join(dirpath, filename))
            file_path, file_name = os.path.split(file)
            file_n, file_ext = os.path.splitext(file_name)
            file_ext = file_ext[1:].lower()

            if file_ext in IGN_EXT:
                continue

            if file_ext in VID_EXT:
                file2 = file.rsplit('.', 1)[0] + ".thm"
                if os.path.exists(file2) and os.path.isfile(file2):
                    camera_file, model_file, dt_file = photo_sup.extract_from_file(file2)
                    camera_exif, model_exif, dt_exif = photo_sup.extract_exif_data(file2)
                    if camera_exif == "Unknown":
                        camera = camera_file
                        info_tag = False
                    else:
                        camera = camera_exif
                        info_tag = True
                    if model_exif == "Unknown":
                        model = model_file
                    else:
                        model = model_exif
                    if dt_exif is None:
                        dt = dt_file
                    else:
                        dt = dt_exif
                else:
                    try:
                        probe = ffmpeg.probe(file)
                        if 'format' in probe and 'tags' in probe['format']:
                            if 'creation_time' in probe['format']['tags']:
                                dt_str = probe['format']['tags']['creation_time']
                                dt = None
                                if dt is None:
                                    try:
                                        dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S.%f%z")
                                    except (ValueError, TypeError) as e:
                                        dt = None
                                if dt is None:
                                    try:
                                        dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
                                        dt = dt.replace(tzinfo=timezone.utc)
                                    except (ValueError, TypeError) as e:
                                        dt = None
                                if dt is None:
                                    print(f'Cant extract date from ffmpge.probe in file {file}')
                            if 'com.android.manufacturer' in probe['format']['tags']:
                                camera = probe['format']['tags']['com.android.manufacturer']
                            if 'com.android.model' in probe['format']['tags']:
                                model = probe['format']['tags']['com.android.model']
                    except (ffmpeg.Error) as e:
                        print("Error reading metadata:", e.stderr.decode())
                    except Exception as e:
                        pass
                if camera == 'Unknown' or dt is None:
                    camera_file, model_file, dt_file = photo_sup.extract_from_file(file)
                    if dt is None:
                        dt = dt_file
                        print(f'Date from file: {file_name}')
                    else:
                        info_date = True
                    if camera == 'Unknown':
                        camera = camera_file
                    else:
                        info_tag = True
                else:
                    info_tag = True
                    info_date = True
            elif file_ext in PIC_EXT:
                camera_file, model_file, dt_file = photo_sup.extract_from_file(file)
                camera_exif, model_exif, dt_exif = photo_sup.extract_exif_data(file)
                if camera_exif == "Unknown":
                    camera = camera_file
                    info_tag = False
                else:
                    camera = camera_exif
                    info_tag = True
                if model_exif == "Unknown":
                    model = model_file
                else:
                    model = model_exif
                if dt_exif is None:
                    dt = dt_file
                else:
                    dt = dt_exif
            else:
                print(f"File not supported {file}")
                continue

            ext_tag = photo_sup.model_to_tag(camera, model)
            rec_list.append({'Path': file_path, 'File': file_name, 'Date': format_record_date(dt), 'Camera': camera, 'Model': model, 'Ext': ext_tag, 'InfoTag': info_tag, 'InfoDate': info_date})

    if info:
        for rec in rec_list:
            print(f"{os.path.join(rec['Path'], rec['File']):82} {rec['Date'] or 'None':34} {rec['Camera']:10} {rec['Model']:10} {rec['Ext']} {rec['InfoTag']} {rec['InfoDate']}")

    for rec in rec_list:
        file_n, file_ext = os.path.splitext(rec['File'])
        file_ext = str.lower(file_ext)
        file_ext = file_ext.replace(".jpeg", '.jpg')

        dt = photo_sup.str_to_dt(rec['Date'])
        if dt is None:
            dt = datetime.now(timezone.utc)
        dt_str = photo_sup.dt_to_str(dt)
        new_name = dt_str + "_" + rec['Ext'] + file_ext

        old_file = os.path.join(rec['Path'], rec['File'])
        new_file = os.path.join(rec['Path'], new_name)
        old_file2 = os.path.join(rec['Path'], rec['File']).rsplit('.', 1)[0] + ".thm"
        if not os.path.exists(old_file2) or not os.path.isfile(old_file2):
            old_file2 = ""
        if str.lower(old_file) != str.lower(new_file):
            while os.path.exists(new_file) and str.lower(old_file) != str.lower(new_file):
                dt_ms = (int(dt.microsecond / 1000) + 1) % 1000
                dt = dt.replace(microsecond=dt_ms * 1000)
                dt_str = photo_sup.dt_to_str(dt)
                new_name = dt_str + "_" + rec['Ext'] + file_ext
                new_file = os.path.join(rec['Path'], new_name)
        rename_list.append({'old_file': old_file, 'old_file2': old_file2, 'new_file': new_file})

    return rec_list, rename_list


def main():
    parser = argparse.ArgumentParser(description="Rename photos and videos into a standardized timestamped format.")
    parser.add_argument("path", nargs="?", default="C:/Temp/Pic", help="Root directory to scan")
    parser.add_argument("--rename", action="store_true", help="Actually rename files after generating the plan")
    parser.add_argument("--no-info", action="store_false", dest="info", help="Suppress the summary listing")
    parser.set_defaults(info=True)
    args = parser.parse_args()

    path = os.path.abspath(args.path)
    rec_list, rename_list = build_plan(path, info=args.info)

    dt_tag = datetime.now().strftime("%Y%m%d_%H%M%S")
    try:
        json_file = os.path.normcase(os.path.join(path, f"photo_info_{dt_tag}.json"))
        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(rec_list, file, indent=4, ensure_ascii=False)
        print(f"Data successfully saved to '{json_file}'")
    except (OSError, IOError) as e:
        print(f"Error writing to file: {e}")
        return 1

    try:
        json_file = os.path.normcase(os.path.join(path, f"photo_ren_{dt_tag}.json"))
        with open(json_file, "w", encoding="utf-8") as file:
            json.dump(rename_list, file, indent=4, ensure_ascii=False)
        print(f"Data successfully saved to '{json_file}'")
    except (OSError, IOError) as e:
        print(f"Error writing to file: {e}")
        return 1

    if args.rename:
        for rec in rename_list:
            if str.lower(rec['old_file']) != str.lower(rec['new_file']):
                os.rename(rec['old_file'], rec['new_file'])

            if rec.get('old_file2'):
                old_file2 = rec['old_file2']
                new_file2 = os.path.splitext(rec['new_file'])[0] + os.path.splitext(old_file2)[1]
                if str.lower(old_file2) != str.lower(new_file2):
                    os.rename(old_file2, new_file2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())