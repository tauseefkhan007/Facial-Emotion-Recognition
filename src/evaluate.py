import numpy as np
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix, classification_report

from dataset_loader import load_dataset

# Emotion names
emotion_labels = [
    "angry",
    "disgust",
    "fear",
    "happy",
    "neutral",
    "sad",
    "surprise"
]

print("Loading test dataset...")

X_test, y_test = load_dataset("dataset/test")
X_test = X_test.reshape(-1, 48, 48, 1)

print("Loading trained model...")
model = load_model("models/emotion_model.keras")

print("Predicting...")

predictions = model.predict(X_test, verbose=1)
y_pred = np.argmax(predictions, axis=1)

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, target_names=emotion_labels))