import ast
import numpy as np
import os
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

#if not __name__ == "__main__":
#    exit()

def extract_from_file(file:str):
    '''
    Docstring for extract_from_file
    
    :param file: Description
    :type file: str full path
    ''' 
    dt = None
    file_path, file_name = os.path.split(file)
    file_n, file_ext = os.path.splitext(file_name)
    file_n = str.upper(file_n)
    # Get file stats to get dates if not found in meta data
    stats = os.stat(file)
    created = datetime.fromtimestamp(stats.st_birthtime)
    last_modified = datetime.fromtimestamp(stats.st_mtime)        
    last_accessed = datetime.fromtimestamp(stats.st_atime)        
    file_dt = min([last_modified, created, last_accessed])
    file_dt = file_dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))

    try:
        # Try to extract from file_n
        if file_n[0:3] == 'PXL':
            dt_str = file_n[4:22]
            camera = 'Google'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[0:3] == 'IOS':
            dt_str = file_n[4:22]
            camera = 'Apple'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[0:9] == 'MESSENGER':
            camera = 'Messenger'
            dt = file_dt
        elif file_n[0:10] == 'SCREENSHOT':
            camera = 'Screenshot'
            dt = file_dt
        elif file_n[0:5] == 'VIDEO':
            dt_str = file_n[6:22]
            camera = 'Olympus'
            dt = datetime.strptime(dt_str, "%Y%m%d%H%M%S")
            dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
        elif file_n[0:5] == 'RECEIVED':
            camera = 'Received'
            dt = file_dt
        elif file_n[0:3] == 'WIN':
            dt_str = file_n[4:21]
            camera = 'Windows'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H_%M_%S")
            dt = dt.replace(tzinfo=ZoneInfo("Europe/Oslo"))
        elif file_n[-3:] == 'PXL':
            dt_str = file_n[0:18]
            camera = 'Google'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[-3:] == 'IOS':
            dt_str = file_n[0:18]
            camera = 'Apple'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[-3:] == 'MES':
            dt_str = file_n[0:18]
            camera = 'Messenger'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[-3:] == 'SCS':
            dt_str = file_n[0:18]
            camera = 'Screenshot'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[-3:] == 'OLY':
            dt_str = file_n[0:18]
            camera = 'Olympus'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[-3:] == 'RCV':
            dt_str = file_n[0:18]
            camera = 'Received'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[-3:] == 'WIN':
            dt_str = file_n[0:18]
            camera = 'Windows'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[-3:] == 'UUU':
            dt_str = file_n[0:18]
            camera = 'Unknown'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        elif file_n[-3:] == 'OOO':
            dt_str = file_n[0:18]
            camera = 'ooo'
            dt = datetime.strptime(dt_str, "%Y%m%d_%H%M%S%f")
            dt = dt.replace(tzinfo=timezone.utc)
        else:
            camera = 'Unknown'
            dt = file_dt
    except (ValueError, TypeError) as e:
        pass

    return camera, dt
