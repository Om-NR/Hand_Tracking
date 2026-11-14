
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from controller import Controller

# Wrapper class so controller.py can access landmarks via .landmark[i]
class HandLandmarksWrapper:
    def __init__(self, landmarks):
        self.landmark = landmarks

# Define hand landmark connections for OpenCV drawing
HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),       # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),       # Index
    (5, 9), (9, 10), (10, 11), (11, 12),  # Middle
    (9, 13), (13, 14), (14, 15), (15, 16),# Ring
    (13, 17), (0, 17), (17, 18), (18, 19), (19, 20) # Pinky
]

cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 60)

# Setup MediaPipe Tasks Hand Landmarker
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    running_mode=vision.RunningMode.IMAGE
)
detector = vision.HandLandmarker.create_from_options(options)

while True:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect landmarks
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=imgRGB)
    results = detector.detect(mp_image)

    if results.hand_landmarks:
        raw_landmarks = results.hand_landmarks[0]

        # Pass landmarks wrapped with .landmark attribute to Controller
        Controller.hand_Landmarks = HandLandmarksWrapper(raw_landmarks)

        # Draw hand lines using OpenCV
        h, w, _ = img.shape
        for p1, p2 in HAND_CONNECTIONS:
            x1, y1 = int(raw_landmarks[p1].x * w), int(raw_landmarks[p1].y * h)
            x2, y2 = int(raw_landmarks[p2].x * w), int(raw_landmarks[p2].y * h)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Draw hand joint dots
        for lm in raw_landmarks:
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)

        # Execute gesture checks
        Controller.update_fingers_status()
        Controller.cursor_moving()
        Controller.detect_scrolling()
        Controller.detect_zoomming()
        Controller.detect_clicking()
        Controller.detect_dragging()

    cv2.imshow('Hand Tracker', img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()