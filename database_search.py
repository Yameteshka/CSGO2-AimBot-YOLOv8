import os
import keyboard
import cv2
import time

save_path = "new_database/"
delay = 1 / 60
counter = 0

os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Could not open video stream.")
    exit()

while True:
    if keyboard.is_pressed("shift"):
        ret, frame = cap.read()
        if not ret:
            print("Could not read frame.")
            break

        frame_cropped = frame[100:, :]

        file_name = f"screenshot_{counter}.png"
        full_path = os.path.join(save_path, file_name)
        cv2.imwrite(full_path, frame_cropped)

        counter += 1
        time.sleep(delay)

    else:
        time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()
