import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("models/emotion_model.keras")

# Emotion labels (must match the training order)
emotion_labels = [
    "angry",
    "disgust",
    "fear",
    "happy",
    "neutral",
    "sad",
    "surprise"
]

# Image to test
image_path = "dataset/test/happy/PrivateTest_10077120.jpg"

# Read image
image = cv2.imread(image_path)

if image is None:
    print("Could not load image!")
    exit()

# Convert to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize to 48x48
image = cv2.resize(image, (48, 48))

# Normalize
image = image.astype("float32") / 255.0

# Add channel dimension
image = np.expand_dims(image, axis=-1)

# Add batch dimension
image = np.expand_dims(image, axis=0)

# Predict
prediction = model.predict(image)

predicted_class = np.argmax(prediction)
confidence = np.max(prediction)

print("Predicted Emotion:", emotion_labels[predicted_class])
print(f"Confidence: {confidence * 100:.2f}%")