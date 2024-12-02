from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
import tempfile
import streamlit as st
from gtts import gTTS
from io import BytesIO

processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

def text_and_speak(text):
  speaker_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
  speaker_embedding = torch.tensor(speaker_dataset[0]["xvector"]).unsqueeze(0)  # Use the first speaker as an example
  inputs = processor(text=text, return_tensors="pt")
  speech_audio = model.generate_speech(inputs["input_ids"], speaker_embedding, vocoder=vocoder)
  #sf.write("speech.wav", speech_audio.numpy(), samplerate=16000)
  # Save the audio to a temporary file
  with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
    sf.write(temp_file.name, speech_audio.numpy(), samplerate=16000)
    audio_path = temp_file.name

  return audio_path
def text_and_speak(text):
    # Function to generate audio from text
    tts = gTTS(text)
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

st.title("Text to Speech")
input_text = st.text_area("Input text", height=200)
if st.button("Generate Audio"):
    if input_text.strip():
        audio = text_and_speak(input_text)
        st.audio(audio, format="audio/mp3", start_time=0)
    else:
        st.warning("Please enter some text to generate audio.")