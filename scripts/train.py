from ultralytics import YOLO

# Train YOLO11n on AiTV dataset
if __name__ == "__main__":
    model = YOLO("weights/yolo11n.pt")   # load YOLO11n weights
    model.train(
        data="data/data.yaml",           # dataset config
        epochs=5,                        # number of epochs
        imgsz=640,                       # image size
        batch=16,                        # batch size
        device=0                         # 0 = first GPU, use 'cpu' if no GPU
    )
    model.val()  # run validation after training