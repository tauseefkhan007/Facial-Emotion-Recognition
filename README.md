# Facial Emotion Recognition

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20-FF6F00?logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5.0-5C3EE8?logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.3-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10-11557C?logo=plotly&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7-F7931E?logo=scikitlearn&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-macOS-000000?logo=apple&logoColor=white)
![IDE](https://img.shields.io/badge/IDE-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success)

A real-time **Facial Emotion Recognition** system built using **Python, TensorFlow, Keras, and OpenCV**.  
The model classifies human facial expressions into **seven emotions** using a **Convolutional Neural Network (CNN)** and supports **real-time webcam-based prediction**.

---

## 📌 Features

- 🎥 Real-time emotion detection using webcam
- 🖼️ Predict emotion from a single image
- 🧠 CNN model built from scratch
- 📊 Training and validation accuracy graphs
- 📈 Model evaluation on test dataset
- 😊 Detects 7 facial emotions:
  - Angry
  - Disgust
  - Fear
  - Happy
  - Neutral
  - Sad
  - Surprise

---

## 🛠️ Tech Stack

- Python 3.11
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn

---

## 📂 Project Structure

```text
Face-Expression-Detector/
│
├── dataset/
│   ├── train/
│   └── test/
│
├── models/
│   └── emotion_model.keras
│
├── results/
│   ├── accuracy.png
│   └── loss.png
│
├── src/
│   ├── train.py
│   ├── model.py
│   ├── dataset_loader.py
│   ├── preprocess.py
│   ├── predict.py
│   ├── webcam.py
│   ├── evaluate.py
│   ├── plot_history.py
│   └── utils.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone <https://github.com/tauseefkhan007/Facial-Emotion-Recognition>
```

Move into the project

```bash
cd Face-Expression-Detector
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Training

```bash
python src/train.py
```

---

## 🎥 Webcam Detection

```bash
python src/webcam.py
```

Press **Q** to quit the webcam.

---

## 🖼️ Predict a Single Image

```bash
python src/predict.py
```

---


## 📈 Model Performance

| Metric | Value |
|--------|------:|
| Test Accuracy | **50.64%** |
| Test Loss | **1.267** |

---

## 📈 Training Graphs

### Accuracy

![Accuracy](results/accuracy.png)

### Loss

![Loss](results/loss.png)

---

## 🔮 Future Improvements

- Data augmentation
- Transfer learning (MobileNetV2 / EfficientNet)
- Better CNN architecture
- Web application using Flask or FastAPI
- Deploy on Hugging Face Spaces or Render
- Mobile application integration

---

## 📚 Dataset

FER-2013 Dataset

- 35,887 grayscale images
- Image size: 48×48
- 7 emotion classes

---

## 👨‍💻 Author

**Tauseef Khan**

- GitHub Profile: https://github.com/tauseefkhan007
- Project Repository: https://github.com/tauseefkhan007/Facial-Emotion-Recognition

---

## 🖥️ Development Environment

- **Device:** Apple MacBook Air
- **Operating System:** macOS
- **Python:** 3.11
- **IDE:** Visual Studio Code

---

## ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.