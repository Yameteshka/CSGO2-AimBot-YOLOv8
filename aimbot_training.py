from ultralytics import YOLO


def main():
    model = YOLO("yolov8s.pt")

    model.train(data="data.yaml", epochs=50, device=0)

    best_model_path = "runs/detect/train/weights/best.pt"
    model = YOLO(best_model_path)


if __name__ == "__main__":
    main()