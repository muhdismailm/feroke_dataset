import cv2
import os
from tqdm import tqdm

video_path = "feroke1.mp4"
output_folder = "frames13"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = int(frame_count / fps)

print("FPS:", fps)
print("Duration:", duration, "seconds")

frame_id = 0

# Progress bar for seconds
for sec in tqdm(range(duration), desc="Extracting Frames"):

    times = [sec*1000 + 1, sec*1000 + 14]

    for t in times:
        cap.set(cv2.CAP_PROP_POS_MSEC, t)
        ret, frame = cap.read()

        if ret:
            filename = f"{output_folder}/frame_{frame_id}.jpg"
            cv2.imwrite(filename, frame)
            frame_id += 1

cap.release()
print("Extraction complete")