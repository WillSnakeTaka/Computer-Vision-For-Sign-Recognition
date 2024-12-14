# 🌟 Signalyze: Sign Language to Text-to-Speech

**Our Designing Document Here**! 🚀 :
[Our Initial Document](https://docs.google.com/document/d/1ewkkNGxOKf1M2MNxaz6vd0o2AKppRD_v_z_kCHBdar4/edit?usp=sharing)

**Our Designing Slides**! 🚀 :
[Our Designing Slides](https://docs.google.com/presentation/d/1apgiMdiOk90Omo3D5VQVxDHyRXxKAYF82B6d1-4a9zY/edit?usp=sharing)

**Our Presentation Page**! 🐍: 
[Visit Our Presentation Page](https://willsnaketaka.github.io/CTP_Presentation_Poorman-s_Version/)

**Our Prototype Link**! 🐍: 
[Visit Hugging face repo)](https://huggingface.co/spaces/curryporkchop/ASLGestureApp)

**Our Youtube Presentation Link**! 🐍: 

[![New Video Thumbnail](https://img.youtube.com/vi/L_AO-OxuEeA/0.jpg)](https://youtu.be/L_AO-OxuEeA)


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
| **OpenCV**       | Image and Video processing   |
| **MediaPipe**    | Hand tracking and gesture detection    |
| **TensorFlow**   | Deep learning model for gesture recognition |
| **Keras**        | Simplified model building and training |
| **gTTS/Pyttsx3** | Text-to-speech synthesis               |
| **Subprocess**   | Text-to-speech MacOs version              |
| **Hugging Face** | Text-to-speech application              |
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


## 📊 General FlowChart

```mermaid
graph TD;
    A[Input: Camera Feed] --> B[OpenCV: Frame Preprocessing];
    B --> C[MediaPipe: Hand Detection];
    C --> D[TensorFlow: Gesture Classification];
    D --> E[Output: Text & Speech];
```

## 📊 Text to Speech

```mermaid
graph TD;
    A[Import Libraries] --> B[Load Pretrained Models];
    B --> C[Load Dataset: Speaker Embeddings];
    C --> D[Process Input Text: Using Processor];
    D --> E[Generate Speech Audio: SpeechT5 Model & Vocoder];
    E --> F[Save Audio File: wav Format];
```






