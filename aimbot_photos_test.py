import cv2
from ultralytics import YOLO


def run_interface(model, cap, confidence_threshold=0.457, output_dir="output_images/"):

    frame_counter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_cropped = frame[100:, :]

        results = model(frame_cropped)

        for result in results:
            boxes = result.boxes

            for box in boxes:
                x1 = y1 = x2 = y2 = None
                label = confidence = None

                if box.conf[0] >= confidence_threshold:
                    x1, y1, x2, y2 = map(int, box.xywh[0])
                    label = result.names[int(box.cls[0])]
                    confidence = box.conf[0]

                    cv2.rectangle(frame_cropped, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame_cropped, f'{label} {confidence:.2f}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        if len(boxes) > 0:
            file_name = f'{output_dir}/frame_{frame_counter}.png'
            cv2.imwrite(file_name, frame_cropped)

        #cv2.imshow('YOLO interface', frame_cropped)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def main():
    model = YOLO("runs/detect/train/weights/best.pt")

    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Could not open video stream or file")
        return

    run_interface(model, cap)


if __name__ == '__main__':
    main()