from ultralytics import YOLO

# Load trained model (best.pt)
model = YOLO("runs/detect/train/weights/best.pt")

# Inference on an image; saves outputs to runs/
results = model("examples/test_images/0.jpg", conf=0.25, save=True)

# If you want to use a video instead, use a file path or webcam index:
# results = model("examples/test_video.mp4", conf=0.25, save=True)
# results = model(0, conf=0.25, save=True)  # webcam