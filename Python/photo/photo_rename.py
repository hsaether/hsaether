import numpy as np
from PIL import Image
from PIL.ExifTags import TAGS
import os

if not __name__ == "__main__":
    exit()
# Open the image file
image = Image.open("C:/Users/Harald/OneDrive/Pictures/2025/Img_9065.jpg")

image = Image.open("C:/Users/Harald/OneDrive/Pictures/2025//PXL_20250823_120342128.jpg")


path = "C:/Users/Harald/OneDrive/Pictures/2025"
files = []

# Traverse directories using os.walk
for dirpath, dirnames, filenames in os.walk(path):
    print(f"Directory: {dirpath}")
    for dirname in dirnames:
        print(f" Subdirectory: {dirname}")
    for filename in filenames:
        print(f" File: {filename}")

exit()
# Extract EXIF data
exif_data = image._exif

# Parse and display metadata
if exif_data:
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag}: {value}")
else:
    print("No EXIF metadata found.")