# 🛰️ AiTV: Disaster-Time Human Detection Dataset

## 📖 Overview
This repository contains the code and information for the project  
**"AiTV: Human Detection in Disaster Scenarios with Real and Night-Time Imagery"**  
developed by *Yusuf Özdemir* as part of a **TÜBİTAK-approved research project**.

The **AiTV dataset** is a novel real-world dataset created to advance human detection in disaster scenarios such as 🌍 **earthquakes**, 🌊 **floods**, 🔥 **wildfires**, and ❄️ **avalanches**.  
✨ Unlike many existing datasets, AiTV also includes **challenging night scenes**, making it a unique and valuable resource for training and benchmarking **YOLO-based object detection models**.

---

## 🔗 Resources
- 📂 **Dataset on Kaggle**: [AiTV Dataset – Human Detection at Disasters](https://www.kaggle.com/datasets/yusufzdemir23/aitv-dataset-human-detection-at-disasters)  
- 🎥 **Demo Video on YouTube**: [Watch Demo](https://www.youtube.com/watch?v=26741W2jWw0)

📂 Dataset Description (AiTV)

The AiTV dataset consists of ~4,000 real images captured from diverse disaster scenarios. It focuses on human detection during critical events and is designed to support research in search-and-rescue applications.

Disaster Scenarios Included
	•	🌍 Earthquake
	•	🌊 Flood
	•	🔥 Wildfire
	•	❄️ Avalanche
	•	🌙 Night-time conditions

⸻

📁 Dataset Structure

The AiTV dataset is organized into training, validation, and test sets in standard YOLO format:

aitv/
│
├── train/
│   ├── images/
│   │   └── [Training image files]
│   └── labels/
│       └── [YOLO format label files for training images]
│
├── val/
│   ├── images/
│   │   └── [Validation image files]
│   └── labels/
│       └── [YOLO format label files for validation images]
│
└── test/
    ├── images/
    │   └── [Test image files]
    └── labels/
        └── [YOLO format label files for test images]

	•	Image Files: Located under the images/ subfolder (JPG/PNG format).
	•	YOLO Annotations: Located under the labels/ subfolder.
  
  Each .txt file has one line per object:
  class x_center y_center width height
  (All coordinates are normalized to [0, 1]).


📌 Usage Notes
	•	The dataset is split into train / val / test to support reproducible experiments.
	•	Annotation format: YOLO (ready to use with Ultralytics YOLO).
	•	Includes night-time images, making the dataset more challenging and unique compared to most disaster datasets.
	•	Focused on a single class (person), ideal for training human detection models.

    ⭐ Key Features
	•	✅ Real disaster imagery (no synthetic scenes)
	•	✅ Challenging night scenes included
	•	✅ ~4,000 labeled images across multiple disaster scenarios
	•	✅ Ready-to-use YOLO format with train/val/test splits
	•	✅ Designed for disaster response & search-and-rescue research

 ## 📊 Benchmarking Summary (YOLO11n vs YOLO11m)

| Disaster Type   | YOLO11n mAP50 | YOLO11n mAP50-95 | YOLO11m mAP50 | YOLO11m mAP50-95 |
|-----------------|---------------|------------------|---------------|------------------|
| 🌍 Earthquake   | 0.91          | 0.56             | 0.93          | 0.60             |
| 🌊 Flood        | 0.89          | 0.55             | 0.91          | 0.58             |
| 🔥 Fire         | 0.92          | 0.57             | 0.94          | 0.61             |
| ❄️ Avalanche    | 0.90          | 0.54             | 0.92          | 0.59             |
| 🌙 Night Scenes | 0.85          | 0.50             | 0.87          | 0.53             |
| **Overall**     | **0.90+**     | **0.55–0.56**    | **0.92+**     | **0.59–0.60**    |