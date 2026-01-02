import numpy as np
#from PIL import Image
#from PIL.ExifTags import TAGS
import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import exifread
from tinytag import TinyTag

from support_functions import string_to_array

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
        _, file_name = os.path.split(file)
        file_n, file_ext = os.path.splitext(file_name)

        # Get file stats to get dates if not found in meta data
        stats = os.stat(file)
        created = datetime.fromtimestamp(stats.st_birthtime)
        last_modified = datetime.fromtimestamp(stats.st_mtime)        
        last_accessed = datetime.fromtimestamp(stats.st_atime)        
        file_dt = min([last_modified, created, last_accessed])
        file_dt = file_dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))

        # Video file
        if str.lower(file_ext) == '.mp4':
            tag = TinyTag.get(file)
            # print(f'{filename}: Title: {tag.title}, Artist: {tag.artist}, Year: {tag.year}')
            if tag.year != None:
                print(f'{filename}: Title: {tag.title}, Artist: {tag.artist}, Year: {tag.year}')
                raise ValueError('TODO Year is found')
            # Extracting from filename
            if file_n[0:3] == 'PXL':
                dt_str = file_n[4:22]
                camera = 'Google'
                dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
                dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
            elif file_n[0:5] == 'video':
                dt_str = file_n[6:22]
                camera = 'Olympus'
                dt = datetime.strptime(dt_str, "%Y%m%d%H%M%S")
                dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
            elif file_n[-3:] == 'iOS':
                dt_str = file_n[0:18]
                camera = 'Apple'
                dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
                dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
            elif file_n[0:9] == 'Messenger':
                camera = 'Messenger'
                dt = file_dt
            else:
                dt = file_dt
        else:            
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
                        dt_str = '1970:01:01 00:00:00.000'
                        dt_str = file_dt.strftime("%Y:%m:%d %H:%M:%S.%f")
                        print(f"Missing Datetime using filetime in {file}")

                    # Converting to dattime format, trying different format
                    dt:datetime = None
                    if dt == None:
                        try:
                            # With ms and timezone
                            dt = datetime.strptime(dt_str, "%Y:%m:%d %H:%M:%S.%f")
                        except ValueError as e:
                            dt:datetime = None
                    if dt == None:
                        try:
                            # format 2025-01-01T12:01:01.001
                            dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S.%f")
                        except ValueError as e:
                            dt:datetime = None

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
                    elif dt != None and dt > datetime(1971,1,1,0,0,0):
                        dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
                else:
                    # Try to extract from filename
                    if file_n[-3:] == 'iOS':
                        dt_str = file_n[0:18]
                        camera = 'Apple'
                        dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
                        dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
                        print(f"NO EXIF metadata found in {file}")
                    elif file_n[0:9] == 'Messenger':
                        camera = 'Messenger'
                        print(f"NO EXIF metadata found, using filetime in {file}")
                        dt = file_dt
                    elif file_n[0:10] == 'Screenshot':
                        camera = 'Screenshot'
                        print(f"NO EXIF metadata found, using filetime in {file}")
                        dt = file_dt
                    else:
                        print(f"NO EXIF metadata found, No Camera info, using filetime in {file}")
                        dt = file_dt
                    
        match camera:
            case 'Canon':
                ext_tag = 'EOS'
            case 'Apple':
                ext_tag = 'iOS'
            case 'Google':
                ext_tag = 'PXL'
            case 'Olympus':
                ext_tag = 'OLY'
            case 'Messenger':
                ext_tag = 'MES'
            case 'Screenshot':
                ext_tag = 'ScS'
            case 'Unknown':
                ext_tag = 'uuu'
            case _: 
                ext_tag = 'ooo'
                    
        rec_list.append({'Path': dirpath, 'File': filename, 'Date': dt, 'Camera': camera, 'Model': model, 'Ext': ext_tag})
        
for rec in rec_list:
    pass
    #print(f'{os.path.join(rec['Path'],rec['File']):82} {rec['Date'].isoformat():34} {rec['Camera']:10} {rec['Model']:10} {rec['Ext']}')

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