import os
import cv2
from PIL import Image
import imagehash
import shutil

input_folder = r"D:\ferok video\feroke Bridge cctv\frames\frames2"
output_folder = r"D:\ferok video\feroke Bridge cctv\clean_frames2"

os.makedirs(output_folder, exist_ok=True)

hashes = []
threshold = 5   # lower = stricter duplicate removal
saved = 0

for file in sorted(os.listdir(input_folder)):
    path = os.path.join(input_folder, file)

    if not file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img = Image.open(path)
    phash = imagehash.phash(img)

    duplicate = False

    for h in hashes:
        if phash - h <= threshold:
            duplicate = True
            break

    if not duplicate:
        hashes.append(phash)
        shutil.copy(path, os.path.join(output_folder, file))
        saved += 1

print("Total frames kept:", saved)
print("Clean frames saved to:", output_folder)