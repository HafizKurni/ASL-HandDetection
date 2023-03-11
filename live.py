import os
import time

from ultralytics import YOLO
import cv2

# model_path = os.path.join('.', 'weights', 'best.pt')
# model_path = 'Colab/HandASL5/yolov8n.pt'

model_path = 'ASL-HandDetection/beste11.pt'
model = YOLO(model_path)
model.predict(source="0", show=True, conf=0.5)

# threshold = 0.5
# class_name_dict = {0: "Hello", 1: "I Love You", 2: "No", 3: "Please", 4: "Thanks", 5: "Yes"}

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#     H, W, _ = frame.shape

#     results = model(frame)[0]

#     for result in results.boxes.data.tolist():
#         x1, y1, x2, y2, score, class_id = result

#         if score > threshold:
#             cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
#             cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

#     cv2.imshow('Live Object Detection', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
