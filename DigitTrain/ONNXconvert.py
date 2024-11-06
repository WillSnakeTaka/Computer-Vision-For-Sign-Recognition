import tensorflow as tf
import tf2onnx

# Load your model
model = tf.keras.models.load_model("/Users/gavtaka/Desktop/BahnMus/Gesamkunstwahnsinn/IndieGame/UnityGaming/MyDigit/DigitTrain/digit_recognizer.h5")

# Set input and output names (customize names if necessary)
input_signature = [tf.TensorSpec(model.input_shape, tf.float32, name="input")]

# Convert to ONNX
onnx_model, _ = tf2onnx.convert.from_keras(
    model,
    input_signature=input_signature,
    opset=13,  # Use a compatible opset for Barracuda; try 13 or adjust if needed
    output_path="/Users/gavtaka/Desktop/BahnMus/Gesamkunstwahnsinn/IndieGame/UnityGaming/MyDigit/DigitTrain/digit_recognizer.onnx")
