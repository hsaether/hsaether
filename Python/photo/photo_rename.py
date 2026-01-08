import numpy as np
import os
import json
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import ffmpeg

import photo_suport as photo_sup

if not __name__ == "__main__":
    exit()

'''
Not all files has meta information about camera.
Not all have timezone information
GPS is not used for timezone
InfoTag means camera from Meta
InfoDate means date from meta
TODO add command line
TODO add thm
TODO tag shall be model EOS500
'''
#path = "C:/Users/Harald/OneDrive/Pictures/2025"
path = "C:/Temp/Pic" 
files = []

record = {}
record['Path'] = ''
record['File'] = ''
record['Date'] = None
record['Camera'] = ''
record['Model'] = ''
record['Ext'] = ''
record['InfoTag'] = False
record['InfoDate'] = False

rec_list = []
rename_list = []

RENAME = False
INFO = True

PIC_EXT = ["jpeg", "jpg", 'dng', "heic", 'png', 'tiff', 'tif', 'crw', 'cr2', 'cr3', 'arw', 'nef']
VID_EXT = ["mp4", "avi", 'mov']
IGN_EXT = ["thm", "info", "json", "pdf", "xls", "xlsx", "doc", "docx", "wks", "htm", "ini", "gif", "wdb", "x3d", "ppt"]

# Traverse directories using os.walk
for dirpath, dirnames, filenames in os.walk(path):
    #print(f"Directory: {dirpath}")
    #for dirname in dirnames:
        #print(f" Subdirectory: {dirname}")
    for filename in filenames:
        exif_data = None
        probe = None
        camera = 'Unknown'
        model = "Unknown"
        ext_tag = 'ooo'
        info_tag = False
        info_date = False
        dt_str = ''
        tz_str = ''
        tz = None
        dt = None

        file = os.path.abspath(os.path.join(dirpath, filename))
        file_path, file_name = os.path.split(file)
        file_n, file_ext = os.path.splitext(file_name)
        file_ext = file_ext[1:].lower()
        file2 = ""

        if file_ext in IGN_EXT:
            continue

        # Video file
        elif file_ext in VID_EXT:
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
                    model= model_file
                else:
                    model = model_exif
                if dt_exif == None:
                    dt = dt_file
                    dt_tag = False
                else:
                    dt = dt_exif
                    dt_tag = True
            else:
                try:
                    probe = ffmpeg.probe(file)
                    if 'format' in probe and 'tags' in probe['format'] :
                        if 'creation_time' in probe['format']['tags']:
                            dt_str = probe['format']['tags']['creation_time']
                            dt = None
                            if dt == None:
                                try:
                                    dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S.%f%z")
                                except (ValueError, TypeError) as e:
                                    dt = None
                            if dt == None:
                                try:
                                    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
                                    dt = dt.replace(tzinfo=timezone.utc)         
                                except (ValueError, TypeError) as e:
                                    dt = None
                            if dt == None:
                                print(f'Cant extract date from ffmpge.probe in file {file}')
                        if 'com.android.manufacturer' in probe['format']['tags']:
                            camera = probe['format']['tags']['com.android.manufacturer']
                        if 'com.android.model' in probe['format']['tags']:
                            model = probe['format']['tags']['com.android.model']
                except (ffmpeg.Error) as e:
                    print("Error reading metadata:", e.stderr.decode())        
                except Exception as e:
                    pass
                    pass
            if camera == 'Unknown' or dt == None:
                # Extracting from filename
                camera_file, model_file, dt_file = photo_sup.extract_from_file(file)
                if dt == None:
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

        # Pictures
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
                model= model_file
            else:
                model = model_exif
            if dt_exif == None:
                dt = dt_file
                dt_tag = False
            else:
                dt = dt_exif
                dt_tag = True
        else:
            print(f"File not supported {file}")
            continue   
        ext_tag = photo_sup.model_to_tag(camera, model)         
                    
        rec_list.append({'Path': file_path, 'File': file_name, 'Date': dt.isoformat(timespec='microseconds'), 'Camera': camera, 'Model': model, 'Ext': ext_tag, 'InfoTag':info_tag, 'InfoDate':info_date})
if INFO:
    for rec in rec_list:
        pass
        print(f'{os.path.join(rec['Path'],rec['File']):82} {rec['Date']:34} {rec['Camera']:10} {rec['Model']:10} {rec['Ext']} {rec['InfoTag']} {rec['InfoDate']}')

# Building renaming dictionary
for rec in rec_list:
    file_n, file_ext = os.path.splitext(rec['File'])
    file_ext = str.lower(file_ext)
    file_ext = file_ext.replace(".jpeg", '.jpg')

    dt = photo_sup.str_to_dt(rec['Date'])
    dt_str = photo_sup.dt_to_str(dt)
    new_name = dt_str + "_" + rec['Ext'] + file_ext
 
    old_file = os.path.join(rec['Path'], rec['File'])
    new_file = os.path.join(rec['Path'], new_name)
    old_file2 = os.path.join(rec['Path'], rec['File']).rsplit('.', 1)[0] + ".thm"
    if not os.path.exists(old_file2) or not os.path.isfile(old_file2):
        old_file2 = ""
    if str.lower(old_file) != str.lower(new_file):
        while os.path.exists(new_file) and str.lower(old_file) != str.lower(new_file):
            dt_ms = (int(dt.microsecond/1000) + 1) % 1000
            dt = dt.replace(microsecond=dt_ms*1000)
            dt_str = photo_sup.dt_to_str(dt)
            new_name = dt_str + "_" + rec['Ext'] + file_ext
            new_file = os.path.join(rec['Path'], new_name)
    #if INFO and str.lower(old_file) != str.lower(new_file): 
    #    print(f'{rec['File']:46} {new_name:30} {rec['Date']:34}')
    rename_list.append({'old_file': old_file, 'old_file2': old_file2, 'new_file': new_file})

# Jason information
dt_tag:str = datetime.now().strftime("%Y%m%d_%H%M%S")
try:
    jason_file = os.path.normcase(os.path.join(path, f"photo_info_{dt_tag}.json"))
    with open(jason_file, "w", encoding="utf-8") as file:
        json.dump(rec_list, file, indent=4, ensure_ascii=False)
    print(f"Data successfully saved to '{jason_file}'")
except (OSError, IOError) as e:
    print(f"Error writing to file: {e}")
    exit()
try:
    jason_file = os.path.normcase(os.path.join(path, f"photo_ren_{dt_tag}.json"))
    with open(jason_file, "w", encoding="utf-8") as file:
        json.dump(rename_list, file, indent=4, ensure_ascii=False)
    print(f"Data successfully saved to '{jason_file}'")
except (OSError, IOError) as e:
    print(f"Error writing to file: {e}")
    exit()


if RENAME:
    for rec in rename_list:
        if str.lower(rec['old_file']) != str.lower(rec['new_file']):
            os.rename(rec['old_file'], rec['new_file'])


exit()

# Extract EXIF data
#exif_data = image._exif

# Parse and display metadata
#if exif_data:
#    for tag_id, value in exif_data.items():
#        tag = TAGS.get(tag_id, tag_id)
#        print(f"{tag}: {value}")
#else:
#    print("No EXIF metadata found.")