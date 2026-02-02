import pyttsx3
import uuid

engine = pyttsx3.init()
engine.setProperty("rate", 160)

def text_to_speech(text: str) -> str:
    filename = f"response_{uuid.uuid4().hex}.mp3"
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename
