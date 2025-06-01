import time
import cv2
from ultralytics import YOLO
import pydirectinput

pydirectinput.FAILSAFE = False


def run_interface(model, cap, confidence_threshold=0.457):
    priority_targets = {"head": 1, "body": 2}

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        time.sleep(0.01)

        frame_cropped = frame[100:, :]
        results = model(frame_cropped)

        target = None
        min_priority = float('inf')

        for result in results:
            boxes = result.boxes

            for box in boxes:
                if box.conf[0] >= confidence_threshold:
                    label = result.names[int(box.cls[0])]
                    if label in priority_targets:
                        priority = priority_targets[label]
                        if priority < min_priority:
                            min_priority = priority
                            x1, y1, x2, y2 = map(int, box.xyxy[0])
                            target = ((x1 + x2) // 2, (y1 + y2) // 2)

                            print(f"Detected {label} at box coordinates: ({x1}, {y1}), ({x2}, {y2})")
                            print(f"Center coordinates on image: ({target[0]}, {target[1]})")

        if target:
            x_target, y_target = target
            frame_width, frame_height = frame_cropped.shape[1], frame_cropped.shape[0]

            screen_width, screen_height = 1920, 1080  # Размеры экрана
            x_absolute = int((x_target / frame_width) * screen_width - 110)
            y_absolute = int((y_target / frame_height) * screen_height - 10)

            print(f"Scaled coordinates to screen: ({x_absolute}, {y_absolute})")

            pydirectinput.moveTo(x_absolute, y_absolute)

    cap.release()


def main():
    model = YOLO("runs/detect/train/weights/best.pt")
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Cannot open the virtual camera")
        return

    run_interface(model, cap)


if __name__ == "__main__":
    main()
