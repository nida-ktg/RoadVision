"""
from ultralytics import YOLO
import cv2

# YOLO modelini yükle
model = YOLO("yolov8n.pt")

# video aç
cap = cv2.VideoCapture("videos/test_video.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # nesne tespiti
    results = model(frame)

    # sonuçları çiz
    annotated_frame = results[0].plot()

    # ekranda göster
    cv2.imshow("Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
"""
