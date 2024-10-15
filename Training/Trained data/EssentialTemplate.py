# import those things
import numpy as np
import pandas as pd
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from sklearn.model_selection import train_test_split

# cleaned data for processing
data = pd.read_csv('path_to_dataset.csv')

# read data
X = data.iloc[:, 1:].values  # Assuming labels are in the first column
y = data.iloc[:, 0].values   # Adjust indexing based on the dataset

# Reshape the features (example: 28x28 images for grayscale data)
X = X.reshape(-1, 28, 28, 1) / 255.0  # Adjust shape as needed (e.g., (width, height, channels))

# Convert labels to categorical 
# The number of classes depends on your dataset
num_classes = 25  # Example for 25 classes
y = to_categorical(y, num_classes)

# Step 3: Split the data into training and test sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# CNNs part !!! This is CNN instruct
#  Define the CNN model
model = Sequential()

# Convolutional layer(s) + MaxPooling layer(s)
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))  model.add(MaxPooling2D(pool_size=(2, 2)))

# Add more convolutional and pooling layers
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the output
model.add(Flatten())

# Fully connected layer
model.add(Dense(128, activation='relu'))

# Dropout to prevent overfitting 
model.add(Dropout(0.5))

# Output layer (number of neurons should match the number of classes)
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
# Adjust epochs, batch_size, and validation split based on your dataset and requirements
model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))

# Step 7: Save the trained model
model.save('trained_model.h5')

# Print a confirmation message
print("Model has been trained and saved as 'trained_model.h5'")
