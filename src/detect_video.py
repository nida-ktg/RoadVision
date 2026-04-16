'''
from ultralytics import YOLO
import cv2

# YOLO modelini yükle
model = YOLO("yolov8n.pt")

# video aç
cap = cv2.VideoCapture("videos/video_2.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # nesne tespiti
    results = model(frame)

    # sonucu çiz
    annotated_frame = results[0].plot()

    # ekranda göster
    cv2.imshow("YOLO Detection", annotated_frame)

    # q'ya basınca çık
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
'''

from ultralytics import YOLO
import cv2
import os

model = YOLO("yolov8n.pt")

video_folder = "videos"

for video_name in os.listdir(video_folder):

    video_path = os.path.join(video_folder, video_name)

    cap = cv2.VideoCapture(video_path)

    print(f"Şu video işleniyor: {video_name}")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame, conf=0.4)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLO Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

cv2.destroyAllWindows()