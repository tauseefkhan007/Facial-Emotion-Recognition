import os
import cv2
import numpy as np

TRAIN_PATH = "dataset/train"

# List of emotions
emotions = sorted(os.listdir(TRAIN_PATH))

print("Emotion Labels:")
for i, emotion in enumerate(emotions):
    print(f"{i} -> {emotion}")

X = []
y = []

for label, emotion in enumerate(emotions):

    emotion_path = os.path.join(TRAIN_PATH, emotion)

    images = os.listdir(emotion_path)

    print(f"\nLoading {emotion} ({len(images)} images)...")

    for image_name in images:

        image_path = os.path.join(emotion_path, image_name)

        image = cv2.imread(image_path)

        if image is None:
            continue

        # Convert to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Normalize
        image = image / 255.0

        X.append(image)
        y.append(label)

X = np.array(X)
y = np.array(y)

print("\nFinished!")
print("Images shape:", X.shape)
print("Labels shape:", y.shape)