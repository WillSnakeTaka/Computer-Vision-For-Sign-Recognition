# import cv2
# import numpy as np
# import tensorflow as tf  # Replace with torch if using PyTorch
# from tensorflow.keras.models import load_model  # For loading CNN models

# # Load the trained CNN model (adjust the path as needed)
# model = load_model("path_to_your_model.h5")  # Replace with your model file

# # Define labels for the classes
# labels = ["Gesture A", "Gesture B", "Gesture C"]  # Replace with your class labels

# # Function to preprocess the frame for the CNN model
# def preprocess_frame(frame, target_size=(224, 224)):
#     # Resize frame to match model input size
#     resized = cv2.resize(frame, target_size)
#     # Normalize pixel values to [0, 1]
#     normalized = resized / 255.0
#     # Add batch dimension
#     batch_frame = np.expand_dims(normalized, axis=0)
#     return batch_frame

# # Function to predict gesture
# def predict_gesture(frame):
#     preprocessed = preprocess_frame(frame)
#     predictions = model.predict(preprocessed)
#     predicted_class = np.argmax(predictions)
#     confidence = np.max(predictions)
#     return labels[predicted_class], confidence

# # Capture video from the webcam
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to grab frame.")
#         break

#     # Preprocess and predict gesture
#     predicted_label, confidence = predict_gesture(frame)

#     # Display prediction on the frame
#     cv2.putText(frame, f"{predicted_label} ({confidence:.2f})",
#                 (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     # Show the frame
#     cv2.imshow("Live Video Feed with Gesture Recognition", frame)

#     # Press 'q' to quit
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Load and preprocess an image
img_path = "path_to_image.jpg"
img = image.load_img(img_path, target_size=(224, 224))  # Resize to 224x224
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
img_array = preprocess_input(img_array)  # Preprocess for MobileNetV2

# Predict using MobileNetV2
predictions = model.predict(img_array)
decoded_predictions = decode_predictions(predictions, top=3)  # Get top-3 predictions
for i, (imagenet_id, label, confidence) in enumerate(decoded_predictions[0]):
    print(f"{i + 1}: {label} ({confidence * 100:.2f}%)")
