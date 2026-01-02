import numpy as np
#from PIL import Image
#from PIL.ExifTags import TAGS
import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import exifread
from tinytag import TinyTag

from support_functions import extract_from_file

if not __name__ == "__main__":
    exit()
# Open the image file
#image = Image.open("C:/Users/Harald/OneDrive/Pictures/2025/Img_9065.jpg")

#image = Image.open("C:/Users/Harald/OneDrive/Pictures/2025//PXL_20250823_120342128.jpg")

'''
Missing handling of meta from MP4
Can maybe extract from filename for some. 
Separation of Video in files is not added yet. 
The timestamp in file seems to be UTC. Canon does not have this meta information.
Decide if to convert to local time or use UTC in files.
currently the records are being buildt.
'''

#path = "C:/Users/Harald/OneDrive/Pictures/2025"
path = "C:/Temp/2025"
files = []

record = {}
record['Path'] = ''
record['File'] = ''
record['Date'] = None
record['Camera'] = ''
record['Model'] = ''
record['Ext'] = ''
rec_list = []

RENAME = False
INFO = True
# Traverse directories using os.walk
for dirpath, dirnames, filenames in os.walk(path):
    #print(f"Directory: {dirpath}")
    #for dirname in dirnames:
        #print(f" Subdirectory: {dirname}")
    for filename in filenames:
        exif_data = None
        tag = None
        camera = 'Unknown'
        model = "Unknown"
        ext_tag = 'ooo'
        dt_str = ''
        tz_str = ''
        tz = None
        dt = None
        dt = datetime(1970,1,1,0,0,0)

        file = os.path.abspath(os.path.join(dirpath, filename))
        file_path, file_name = os.path.split(file)
        file_n, file_ext = os.path.splitext(file_name)

        # Video file
        if str.lower(file_ext) == '.mp4':
            tag = TinyTag.get(file)
            # print(f'{filename}: Title: {tag.title}, Artist: {tag.artist}, Year: {tag.year}')
            if tag.year != None:
                print(f'{filename}: Title: {tag.title}, Artist: {tag.artist}, Year: {tag.year}')
                raise ValueError('TODO Year is found')
            # Extracting from filename
            camera, dt = extract_from_file(file)
            if camera == 'Unknown':
                print(f'Date from file: {file_name}')
        else:            
            camera, dt = extract_from_file(file)
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
                    if 'Image Model' in exif_data:
                        try:
                            model = ''.join(chr(i) for i in exif_data['Image Model'].values)
                        except (ValueError, TypeError) as e:
                            model = exif_data['Image Model'].values
                        model = model.replace('Canon ', '')
                        model = model.replace('Olympus ', '')

                    # Time ms
                    if 'EXIF SubSecTime' in exif_data:
                        ms_str = "." + exif_data['EXIF SubSecTime'].values
                    elif 'EXIF SubSecTimeOriginal' in exif_data:
                        ms_str = "." + exif_data['EXIF SubSecTimeOriginal'].values
                    elif 'EXIF SubSecTimeDigitized' in exif_data:
                        ms_str = "." + exif_data['EXIF SubSecTimeOriginal'].values
                    else:
                        ms_str = ".000"
                    # TODO add from file

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
                    
        match str.lower(camera):
            case 'canon':
                ext_tag = 'EOS'
            case 'apple':
                ext_tag = 'iOS'
            case 'google':
                ext_tag = 'PXL'
            case 'olympus':
                ext_tag = 'OLY'
            case 'messenger':
                ext_tag = 'MES'
            case 'screenshot':
                ext_tag = 'ScS'
            case 'received':
                ext_tag = 'RCV'
            case 'windows':
                ext_tag = 'WIN'
            case 'unknown':
                ext_tag = 'uuu'
            case 'ooo':
                ext_tag = 'ooo'
            case _: 
                ext_tag = 'ooo'
                    
        rec_list.append({'Path': file_path, 'File': file_name, 'Date': dt, 'Camera': camera, 'Model': model, 'Ext': ext_tag})
if INFO:
    for rec in rec_list:
        pass
        print(f'{os.path.join(rec['Path'],rec['File']):82} {rec['Date'].isoformat():34} {rec['Camera']:10} {rec['Model']:10} {rec['Ext']}')

# Renaming
for rec in rec_list:
    file_n, file_ext = os.path.splitext(rec['File'])
    file_ext = str.lower(file_ext)
    file_ext = file_ext.replace(".jpeg", '.jpg')

    dt:datetime = rec['Date']
    dt_ms = int(dt.microsecond/1000)
    new_name = dt.astimezone(timezone.utc).strftime("%Y%m%d_%H%M%S") + f"{dt_ms:03d}" + "_" + rec['Ext'] + file_ext
 
    old_file = os.path.join(rec['Path'], rec['File'])
    new_file = os.path.join(rec['Path'], new_name) 
    if str.lower(old_file) != str.lower(new_file):
        while os.path.exists(new_file) and str.lower(old_file) != str.lower(new_file):
            dt_ms = (dt_ms + 1) % 1000
            new_name = dt.astimezone(timezone.utc).strftime("%Y%m%d_%H%M%S") + f"{dt_ms:03d}" + "_" + rec['Ext'] + file_ext
            new_file = os.path.join(rec['Path'], new_name)
    if INFO and str.lower(old_file) != str.lower(new_file): 
        print(f'{rec['File']:46} {new_name:30} {rec['Date'].isoformat():34}')
    if RENAME:
        os.rename(old_file, new_file)
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