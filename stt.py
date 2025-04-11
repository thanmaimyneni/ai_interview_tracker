# backend/services/stt.py

import speech_recognition as sr

def listen_to_user() -> str:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening... Please speak now.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print(" Could not understand audio.")
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        print(" Could not request results from Google STT service.")
        return "Speech service is currently unavailable."
