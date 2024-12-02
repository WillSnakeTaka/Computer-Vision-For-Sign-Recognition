# 🌟 Signalyze: Sign Language to Text-to-Speech

**Our Designing Document Here**! 🚀 :
https://docs.google.com/document/d/1ewkkNGxOKf1M2MNxaz6vd0o2AKppRD_v_z_kCHBdar4/edit?usp=sharing

---

## 📖 Overview

Signalyze is an application that recognizes sign language gestures in webcam captions and then converts them into texts and speech, which will be benefitial for the deaf and hard-of-hearing communities.

### 🧩 Key Features:
- **Real-Time Gesture Recognition**: Capture and classify hand gestures instantly through Flask app, and webcap caption.
- **Text and Speech Output**: Convert recognized gestures into plain text and converted it into speech.
- **Flask app**: Simple and flexible app for presentation.



---

## 🛠️ Technologies Used

| Technology      | Purpose                                |
|------------------|----------------------------------------|
| **OpenCV**       | Real-time image and video processing   |
| **MediaPipe**    | Hand tracking and gesture detection    |
| **TensorFlow**   | Deep learning model for gesture recognition |
| **Keras**        | Simplified model building and training |
| **gTTS/Pyttsx3** | Text-to-speech synthesis               |
| **Flask**        | Backend for app integration            |
| **NumPy**        | Data manipulation                     |

---

Setup

Navigate to the directory where you want to clone/run/save the application:

cd your_selected_directory
Clone this repository:

git clone [https://github.com/.git](https://github.com/WillSnakeTaka/Signalyze.git)
Navigate to the Signalyze git repository:

cd Signalyzen
Use Python3 3.10 version in the cloned repository folder:

pyenv local 3.10
Create virtual environment in the cloned repository folder:

python -m venv .app.py

## 🔬 Methods:

1. **Data Preparation**:
   - Use datasets like Sign Language MNIST (via Kaggle).
   - Normalize and augment data for enhanced model performance.

2. **Model Development**:
   - Build and train a **Convolutional Neural Network (CNN)** for gesture classification.
   - Evaluate and fine-tune the model for real-world performance.

3. **Applying blueprints into practice**:
   - Using flask and html to call OpenCV.
   - Use MediaPipe for efficient hand tracking and gesture recognition.

4. **Text-to-Speech Integration**:
   - Using pretraining llm for hugging,  .
   - Convert text into speech using gTTS or Pyttsx3.

5. **App Deployment**:
   - Build a user-friendly interface using Flask.
   - Enable real-time classification and output.

---

## 📊 System Workflow

```mermaid
graph TD;
    A[Input: Camera Feed] --> B[OpenCV: Frame Preprocessing];
    B --> C[MediaPipe: Hand Detection];
    C --> D[TensorFlow: Gesture Classification];
    D --> E[Output: Text & Speech];



