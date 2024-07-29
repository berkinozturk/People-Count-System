import cv2
import numpy as np
from ultralytics import YOLO

# Model
yolo_model = YOLO("yolov8l.pt")


def mouse_event_handler(event, x, y, flags, param):
    global start_x, start_y, is_drawing, current_frame

    if event == cv2.EVENT_LBUTTONDOWN:
        is_drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE and is_drawing:
        temp_frame = current_frame.copy()
        cv2.rectangle(temp_frame, (start_x, start_y), (x, y), (0, 255, 0), 2)
        cv2.imshow('Video', temp_frame)

    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False
        rectangles.append((start_x, start_y, x, y))


def draw_detected_people(frame, results):
    labels = results[0].names
    for rect in rectangles:
        person_count = 0
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
        region = np.array([(rect[0], rect[1]), (rect[2], rect[1]), (rect[2], rect[3]), (rect[0], rect[3])])
        region = region.reshape((-1, 1, 2))
        cv2.polylines(frame, [region], True, (0, 255, 255), 5)

        for i in range(len(results[0].boxes)):
            x1, y1, x2, y2 = results[0].boxes.xyxy[i]
            class_id = results[0].boxes.cls[i]
            class_name = labels[int(class_id)]

            if class_name != 'person':
                continue

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            if cv2.pointPolygonTest(region, (center_x, center_y), False) > 0:
                person_count += 1

        cv2.putText(frame, str(person_count), (rect[0], rect[1] - 10), text_font, 1.0, (255, 0, 255), 2)


rectangles = []
is_drawing = False
start_x, start_y = -1, -1

video_capture = cv2.VideoCapture('people1.mp4')
text_font = cv2.QT_FONT_BLACK

cv2.namedWindow('Video')
cv2.setMouseCallback('Video', mouse_event_handler)

while True:
    ret, current_frame = video_capture.read()

    if not ret:
        break

    rgb_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
    detection_results = yolo_model(rgb_frame, verbose=False)

    draw_detected_people(current_frame, detection_results)

    cv2.imshow('Video', current_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
