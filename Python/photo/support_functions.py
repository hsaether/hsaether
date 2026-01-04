import ast
import numpy as np
import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

#if not __name__ == "__main__":
#    exit()

CAMERA_TAG = {'EOS': 'Canon',
              'IXU': 'Canon',
              'CAN': 'Canon',
              'NIK': 'Nikon',
              'DCS': 'Nikon',
              'PTX': 'Pentax',
              'OLY': 'Olympus',
              'iOS': 'Apple',
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

def extract_from_file(file:str):
    '''
    Docstring for extract_from_file
    
    :param file: Description
    :type file: str full path
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

    try:
        # Try to extract from file_n
        # Prefix from some files
        if file_n[0:3] in CAMERA_TAG_LC:
            camera = CAMERA_TAG_LC[file_n[0:3]]
            dt = None
            if dt == None:
                try:
                    dt_str = file_n[4:22]
                    dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
                    dt = dt.replace(tzinfo=timezone.utc)
                except (ValueError, TypeError) as e:
                    dt = None
            if dt == None:
                try:
                    dt_str = file_n[4:21]
                    dt = datetime.strptime(dt_str, "%Y%m%d_%H_%M_%S")
                    dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
                except (ValueError, TypeError) as e:
                    dt = None
            if dt == None:
                print(f'Cant extract date from file for prefix in file {file}')
                dt = file_dt

        # Postfix normally from this program
        elif file_n[-3:] in CAMERA_TAG_LC:
            camera = CAMERA_TAG_LC[file_n[-3:]]
            dt = None
            if dt == None:
                try:
                    dt_str = file_n[0:18]
                    dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
                    dt = dt.replace(tzinfo=timezone.utc)
                except (ValueError, TypeError) as e:
                    dt = None
            if dt == None:
                print(f'Cant extract date from file for prefix in file {file}')
                dt = file_dt

        elif file_n[0:9] == 'messenger':
            camera = 'Messenger'
            dt = file_dt
        elif file_n[0:10] == 'screenshot':
            camera = 'Screenshot'
            dt = file_dt
        elif file_n[0:5] == 'video':
            dt_str = file_n[6:22]
            camera = 'Olympus'
            dt = datetime.strptime(dt_str, "%Y%m%d%H%M%S")
            dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
        elif file_n[0:5] == 'received':
            camera = 'Received'
            dt = file_dt
        else:
            camera = 'Unknown'
            dt = file_dt
    except (ValueError, TypeError) as e:
        pass

    return camera, dt

def camera_to_tag(camera:str, model:str='') -> str:
    camera = str.lower(camera)
    model = str.lower(model)
    ext_tag = 'ooo'

    k = [key for key, value in CAMERA_TAG.items() if value.lower() == camera]
    if len(k) == 1:
        ext_tag = k[0]
    else:
        match camera:
            case 'canon':
                if 'eos' in model:
                    ext_tag = 'EOS'
                elif 'ixus' in model:
                    ext_tag = 'IXU'
                else:
                    ext_tag = 'CAN'
            case 'nikon':
                if 'e3200' in model:
                    ext_tag = 'DCS'
                else:
                    ext_tag = 'NIK'
    if ext_tag == 'ooo':
        pass
    return ext_tag
