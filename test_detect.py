# test_detect.py
from ultralytics import YOLO

model = YOLO("model/soccer_yolov5_custom.pt")
results = model("videos/tacticam.mp4", show=True)
