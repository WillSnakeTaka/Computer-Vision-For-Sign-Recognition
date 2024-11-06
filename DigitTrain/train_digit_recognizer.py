import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Step 1: Load and Preprocess the Data
train_data_path = "/Users/gavtaka/Desktop/BahnMus/Gesamkunstwahnsinn/IndieGame/UnityGaming/MyDigit/DigitTrain/TrainingSample"
datagen = ImageDataGenerator(rescale=1.0/255.0, validation_split=0.2)

print("Starting data loading...")
train_data = datagen.flow_from_directory(
    train_data_path, target_size=(28, 28), color_mode='grayscale', class_mode='sparse',
    batch_size=32, subset='training'
)
val_data = datagen.flow_from_directory(
    train_data_path, target_size=(28, 28), color_mode='grayscale', class_mode='sparse',
    batch_size=32, subset='validation'
)
print("Data loaded.")

# Step 2: Define and Compile the Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')  # 10 outputs for digits 0 to 9
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Step 3: Train the Model
print("Starting model training...")
model.fit(train_data, epochs=5, validation_data=val_data)
print("Training complete.")

# Step 4: Save the Model in `SavedModel` format
# Save the model in `.h5` format
model_save_path = "/Users/gavtaka/Desktop/BahnMus/Gesamkunstwahnsinn/IndieGame/UnityGaming/MyDigit/DigitTrain/digit_recognizer.h5"
model.save(model_save_path)
print(f"Model saved as '{model_save_path}' in H5 format.")

