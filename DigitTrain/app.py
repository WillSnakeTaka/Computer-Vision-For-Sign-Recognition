from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io
import base64

app = Flask(__name__)
model = load_model("digit_recognizer.h5")  # Load your .h5 model here

def preprocess_image(img):
    img = img.resize((28, 28)).convert("L")  # Resize and convert to grayscale (28x28 for MNIST)
    img = np.array(img) / 255.0  # Normalize pixel values
    img = img.reshape(1, 28, 28, 1)  # Reshape for model input
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get image data from request
    img_data = base64.b64decode(data['image'].split(",")[1])  # Decode image data

    # Process the image
    img = Image.open(io.BytesIO(img_data))
    processed_img = preprocess_image(img)

    # Predict using the model
    prediction = model.predict(processed_img)
    predicted_class = np.argmax(prediction[0])

    return jsonify({'prediction': int(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

