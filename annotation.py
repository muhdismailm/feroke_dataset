from ultralytics import YOLO
import os

model = YOLO("yolov8x.pt")  # pretrained model

image_folder = r"D:\ferok video\feroke Bridge cctv\clean_frames2"

model.predict(
    source=image_folder,
    save=True,
    save_txt=True,   # saves labels
    conf=0.25
)