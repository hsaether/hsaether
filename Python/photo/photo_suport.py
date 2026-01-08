import ast
import numpy as np
import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import exifread

#if not __name__ == "__main__":
#    exit()

CAMERA_TAG = {'iOS': 'Apple',
              'PXL': 'Google',
              'GLX': 'Samsung',
              'HTC': 'HTC',
              'ScS': 'Screenshot',
              'RCV': 'Received',
              'WIN': 'Windows',
              'MES': 'Messenger',
              'uuu': 'Unknown',
              }

CAMERA_TAG_LC = {k.lower(): CAMERA_TAG[k] for k in CAMERA_TAG}   

CAMERA_MODEL_TAG = {('CANON', 'EOS R5'):        'EOSR5',
                    ('CANON', 'EOS 500D'):      'EOS500',
                    ('CANON', 'EOS 300D'):      'EOS300',
                    ('CANON', 'IXUS 700'):      'CIX700',
                    ('CANON', 'IXUS 500'):      'CIX500',
                    ('CANON', 'UNKNOWN'):       'CANO', 
                    ('NIKON', 'E3200'):         'NE3200',
                    ('NIKON', 'E2500'):         'NE2500',
                    ('PENTAX', 'OPTIO 50'):     'POPT50',
                    ('APPLE', 'IPHONE 12 PRO'): 'IP12P',
                    ('APPLE', 'IPHONE 4'):      'IP4',
                    ('APPLE', 'UNKNOWN'):       'IPHN',
                    ('OLYMPUS', 'UNKNOWN'):     'OLYM',
                    ('OLYMPUS', 'EP50'):        'EP50',
                    ('GOOGLE', 'PIXEL 7'):      'PXL7',
                    ('GOOGLE', 'UNKNOWN'):      'GOOG',
                    ('SAMSUNG', 'GT-I9100'):    'SGSII',
                    ('SAMSUNG', 'SM-A520F'):    'SGSA5',
                    ('SAMSUNG', 'DIGIMAX L60'): 'SDIL60',
                    ('SAMSUNG', 'SM-T500'):     'STA7',
                    ('HTC', 'S710'):            'HS710',
                    ('SCREENSHOT', 'UNKNOWN'):  'SCRN',
                    ('MESSENGER', 'UNKNOWN'):   'MESN',
                    ('RECEIVED', 'UNKNOWN'):    'RECV',
                    ('WINDOWS','UNKNOWN'):      'WIND',
                    ('UNKNOWN','UNKNOWN'):      'UNKN',
}

def extract_from_file(file:str):
    '''
    Docstring for extract_from_file
    
    :param file: Description
    :type file: str full path
    : return (camera, model)
    ''' 
    dt = None
    file_path, file_name = os.path.split(file)
    file_n, file_ext = os.path.splitext(file_name)
    file_n = str.lower(file_n)
    # Get file stats to get dates if not found in meta data
    stats = os.stat(file)
    created = datetime.fromtimestamp(stats.st_birthtime)
    last_modified = datetime.fromtimestamp(stats.st_mtime)        
    last_accessed = datetime.fromtimestamp(stats.st_atime)        
    file_dt = min([last_modified, created, last_accessed])
    file_dt = file_dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
    model = 'Unknown'

    try:
        # Try to extract from file_n
        # Prefix from some files
        file_split = file_n.split('_')
        start = len(file_split[0])+1

        if file_split[0] in CAMERA_TAG_LC:
            camera = CAMERA_TAG_LC[file_split[0]]
            dt = None
            if dt == None:
                try:
                    stop = start + 18
                    dt_str = file_n[start:stop]
                    dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
                    dt = dt.replace(tzinfo=timezone.utc)
                except (ValueError, TypeError) as e:
                    dt = None
            if dt == None:
                try:
                    stop = start + 17
                    dt_str = file_n[start:stop]
                    dt = datetime.strptime(dt_str, "%Y%m%d_%H_%M_%S")
                    dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
                except (ValueError, TypeError) as e:
                    dt = None
            if dt == None:
                print(f'Cant extract date from file for prefix in file {file}')
                dt = file_dt

        elif file_split[0] == 'messenger':
            camera = 'Messenger'
            dt = file_dt
        elif file_split[0] == 'screenshot':
            camera = 'Screenshot'
            stop = start + 15
            dt_str = file_n[start:stop]
            try:
                dt = datetime.strptime(dt_str, "%Y%m%d-%H%M%S")
                dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
            except (ValueError, TypeError) as e:
                dt = file_dt
        elif file_split[0] == 'video':
            stop = start + 14
            dt_str = file_n[start:stop]
            camera = 'Olympus'
            dt = datetime.strptime(dt_str, "%Y%m%d%H%M%S")
            dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
        elif file_split[0] == 'received':
            camera = 'Received'
            dt = file_dt
        elif file_split[0] == 'img' and len(file_n)>=22:
            camera = 'Unknown'
            try:
                stop = start + 19
                dt_str = file_n[start:stop]
                dt = datetime.strptime(dt_str, "%Y-%m-%d_%H-%M-%S")
                dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
            except (ValueError, TypeError) as e:
                dt = file_dt
        # Postfix Tag
        elif file_split[-1] in CAMERA_TAG_LC:
            camera = CAMERA_TAG_LC[file_split[-1]]
            dt = None
            if dt == None:
                dt_str = file_n[0:18]
                dt = str_to_dt(dt_str)
            if dt == None:
                print(f'Cant extract date from file for prefix in file {file}')
                dt = file_dt
        # Postfix from this program
        elif file_split[-1] in CAMERA_MODEL_TAG.values():
            (camera, model) = [key for key, value in CAMERA_MODEL_TAG() if value == file_split[-1]][0]
            dt = None
            if dt == None:
                dt_str = file_n[0:18]
                dt = str_to_dt(dt_str)
            if dt == None:
                print(f'Cant extract date from file for prefix in file {file}')
                dt = file_dt
        else:
            camera = 'Unknown'
            dt_str = file_n[0:15]
            try:
                dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S")
                dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
            except (TypeError, ValueError) as e:
                dt = None
            if dt == None:
                dt = file_dt
    except (ValueError, TypeError) as e:
        pass

    return camera, model, dt

def model_to_tag(camera:str, model:str) -> str:
    camera = camera.upper()
    model = model.upper()
    tag = 'OOO'

    if (camera, model) in CAMERA_MODEL_TAG:
       tag = CAMERA_MODEL_TAG[(camera, model)] 
    else:
        tag == 'OOO'
    return tag

def dt_to_str(dt:datetime) -> str:
    '''
    Docstring for dt_to_str
    Standard printout for file genration

    :param dt: Description
    :type dt: datetime
    :return: Description
    :rtype: str
    '''
    dt_ms = int(dt.microsecond/1000)
    dt_str = dt.astimezone(timezone.utc).strftime("%Y%m%d_%H%M%S") + f"{dt_ms:03d}"
    return dt_str

def str_to_dt(dt_str:str) -> datetime:
    '''
    Docstring for str_to_dt
    Standard printout for file genration

    :param dt_str: Description
    :type dt_str: str
    :return: datetime 
    :rtype: datetime
    '''
    dt = None
    if dt == None and len(dt_str) == 18:
        try:
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        except (TypeError, ValueError) as e:
            dt = None
    if dt == None and len(dt_str) == 15:
        try:
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S")
            dt = dt.replace(tzinfo=timezone.utc)
        except (TypeError, ValueError) as e:
            dt = None
    if dt == None:
        # try with iso format
        try:
            dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S.%f%z")
        except (ValueError, TypeError) as e:
            dt = None        
    if dt == None:
        # try with iso format without us
        try:
            dt = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%S%z")
        except (ValueError, TypeError) as e:
            dt = None        
    if dt == None:
        print(f"Invalid date conversion for datestring {dt_str}")
    return dt

def extract_exif_data(file:str):
    camera = "Unknown"
    model = "Unknown"
    dt = None
    if not isinstance(file, str) or not file.strip():
        raise ValueError("Invalid file path. Must be a non-empty string.")    
    if not os.path.exists(file) or not os.path.isfile(file):
        return (camera, model, dt)
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

            if dt != None:
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
            if camera == "Unknown":
                pass
        else:
            print(f"NO EXIF metadata found in {file}")
    return (camera, model, dt)
