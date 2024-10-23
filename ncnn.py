from ultralytics import YOLO
model = YOLO("last.pt")
model.export(format="ncnn")