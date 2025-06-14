from yolomodel.detector import detect_on_image
from tts.tts_engine import speak_text
from vision.describer import describe_scene_tinyllama
from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

image_path = r"assets\pedestrian-person-road-traffic-street-car-night-adventure-backpack-driving-city-taxi-cab-transport-evening-vehicle-color-lights-infrastructure-1083012-111143950.jpg"

if os.path.exists(image_path):
    results = detect_on_image(image_path)
    detections = []
    c=0
    for box in results.boxes:
        c+=1
        print(c)
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        cls_id = int(box.cls[0].item())
        label = model.names[cls_id]
        detections.append({"label": label, "bbox": [x1, y1, x2, y2]})
        
    print(detections)

    spoken = describe_scene_tinyllama(detections, frame_width=640)
    print("Description:", spoken)
    speak_text(spoken)
else:
    print("Invalid image path.")
