from tensorflow.keras.callbacks import EarlyStopping
from plot_history import plot_history
import numpy as np
import tensorflow as tf

from dataset_loader import load_dataset
from model import build_model

# Set random seed
np.random.seed(42)
tf.random.set_seed(42)

print("Loading Training Dataset...\n")
X_train, y_train = load_dataset("dataset/train")

print("\nLoading Test Dataset...\n")
X_test, y_test = load_dataset("dataset/test")

print("\nDatasets Loaded Successfully!")

print("Training Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

# Add channel dimension
X_train = X_train.reshape(-1, 48, 48, 1)
X_test = X_test.reshape(-1, 48, 48, 1)

print("New Training Shape:", X_train.shape)
print("New Test Shape:", X_test.shape)

# Build model
model = build_model()

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\nModel compiled successfully!")

# Print model architecture
model.summary()

# Early Stopping
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True
)

# Train model
history = model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=32,
    validation_data=(X_test, y_test),
    callbacks=[early_stop]
)

# Save model
model.save("models/emotion_model.keras")

# Plot graphs
plot_history(history)

print("\nModel saved successfully!")

# Evaluate model
test_loss, test_accuracy = model.evaluate(X_test, y_test)

print("\nTest Accuracy:", test_accuracy)
print("Test Loss:", test_loss)