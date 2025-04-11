# backend/services/tts.py

import pyttsx3

# Initialize TTS engine only once
engine = pyttsx3.init()

# Optional: customize voice and rate
engine.setProperty('rate', 165)  # Speaking speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0=Male, 1=Female (varies by OS)

def speak(text: str):
    print(f"🤖 HR Bot says: {text}")
    engine.say(text)
    engine.runAndWait()
