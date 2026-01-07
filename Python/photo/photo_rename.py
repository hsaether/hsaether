import numpy as np
import os
import json
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import exifread
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

        if file_ext in IGN_EXT:
            continue

        # Video file
        elif file_ext in VID_EXT:
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
            camera, model, dt = photo_sup.extract_from_file(file)
            with open(file, "rb") as file_:
                # Extract metadata
                exif_data = exifread.process_file(file_)
                if exif_data:
                    #for tag_id, value in exif_data.items():
                        #tag = TAGS.get(tag_id, tag_id)
                        #print(f"{tag}: {value}")
                    if 'Image Make' in exif_data:
                        try:
                            camera = ''.join(chr(i) for i in exif_data['Image Make'].values)
                        except (ValueError, TypeError) as e:
                            camera = exif_data['Image Make'].values
                        camera = camera.replace(' Soft Imaging Solutions', '')   
                        camera = camera.replace(' Corporation', '')
                        camera = camera.replace('SAMSUNG TECHWIN CO., LTD.', 'Samsung')
                        info_tag = True
                    if 'Image Model' in exif_data:
                        try:
                            model = ''.join(chr(i) for i in exif_data['Image Model'].values)
                        except (ValueError, TypeError) as e:
                            model:str = exif_data['Image Model'].values
                        model = model.upper()
                        model = model.replace(f"{camera.upper()} ", '')
                        model = model.replace(f"{camera.upper()}_", '')
                        model = model.replace(' DIGITAL', '')
                        model = model.replace('DIGITAL ', '')
                        pass

                    # Time ms
                    if 'EXIF SubSecTime' in exif_data:
                        ms_str = "." + exif_data['EXIF SubSecTime'].values
                    elif 'EXIF SubSecTimeOriginal' in exif_data:
                        ms_str = "." + exif_data['EXIF SubSecTimeOriginal'].values
                    elif 'EXIF SubSecTimeDigitized' in exif_data:
                        ms_str = "." + exif_data['EXIF SubSecTimeOriginal'].values
                    else:
                        ms_str = ".000"

                    # Datetime
                    if 'Image DateTime' in exif_data:
                        dt_str = str(exif_data['Image DateTime']) + ms_str
                    elif 'EXIF DateTimeOriginal' in exif_data:
                        dt_str = str(exif_data['EXIF DateTimeOriginal']) + ms_str
                    elif 'EXIF DateTimeDigitized' in exif_data:
                        dt_str = str(exif_data['EXIF DateTimeDigitized']) + ms_str
                    else:
                        dt_str = None

                    # Converting to dattime format, trying different format
                    dt_conv = None
                    if dt_str != None and dt_conv == None:
                        try:
                            # With ms and timezone
                            dt_conv = datetime.strptime(dt_str, "%Y:%m:%d %H:%M:%S.%f")
                        except ValueError as e:
                            dt_conv = None
                    if dt_str != None and dt_conv == None:
                        try:
                            # format 2025-01-01T12:01:01.001
                            dt_conv = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S.%f")
                        except ValueError as e:
                            dt_conv = None
                    if dt_conv != None:
                        dt = dt_conv
                        info_date = True

                    # Adding timezone
                    if 'EXIF OffsetTime' in exif_data:
                        tz_str = str(exif_data['EXIF OffsetTime'])
                        tz = datetime.strptime(tz_str, "%z").tzinfo
                        dt = dt.replace(tzinfo=tz)
                    elif 'EXIF OffsetTimeOriginal' in exif_data:
                        tz_str = str(exif_data['EXIF OffsetTimeOriginal'])
                        tz = datetime.strptime(tz_str, "%z").tzinfo
                        dt = dt.replace(tzinfo=tz)                        
                    elif 'EXIF OffsetTimeDigitized' in exif_data:
                        tz_str = str(exif_data['EXIF OffsetTimeDigitized'])
                        tz = datetime.strptime(tz_str, "%z").tzinfo
                        dt = dt.replace(tzinfo=tz)                        
                    elif dt.tzinfo == None:
                        dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
                else:
                    print(f"NO EXIF metadata found in {file}")
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

    if str.lower(old_file) != str.lower(new_file):
        while os.path.exists(new_file) and str.lower(old_file) != str.lower(new_file):
            dt_ms = (int(dt.microsecond/1000) + 1) % 1000
            dt = dt.replace(microsecond=dt_ms*1000)
            dt_str = photo_sup.dt_to_str(dt)
            new_name = dt_str + "_" + rec['Ext'] + file_ext
            new_file = os.path.join(rec['Path'], new_name)
    if INFO and str.lower(old_file) != str.lower(new_file): 
        print(f'{rec['File']:46} {new_name:30} {rec['Date']:34}')
    rename_list.append({'old_file': old_file, 'new_file': new_file})

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