from ultralytics import YOLO


def main():
    best_model_path = "runs/detect/train/weights/best.pt"
    model = YOLO(best_model_path)

    images_path = "test/images/"
    confidence_threshold = 0.457

    model.val(data="data.yaml", split='test', conf=confidence_threshold)


if __name__ == "__main__":
    main()