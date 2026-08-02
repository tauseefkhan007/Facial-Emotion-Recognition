import os
import cv2
import numpy as np


def load_dataset(dataset_path):

    emotions = sorted(os.listdir(dataset_path))

    X = []
    y = []

    print("Loading Dataset...\n")

    for label, emotion in enumerate(emotions):

        emotion_path = os.path.join(dataset_path, emotion)

        images = os.listdir(emotion_path)

        print(f"{emotion}: {len(images)} images")

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

    X = np.array(X, dtype=np.float32)
    y = np.array(y)

    return X, y