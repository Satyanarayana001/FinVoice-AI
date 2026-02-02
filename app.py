from fastapi import FastAPI, UploadFile, File
import shutil
import uuid

from stt import speech_to_text
from tts import text_to_speech
from llm import get_llm_response
from intent_router import detect_intent
from context_manager import ConversationManager

app = FastAPI(title="FinVoice-AI")

conversation = ConversationManager()

@app.post("/voice")
async def voice_chat(audio: UploadFile = File(...)):
    filename = f"input_{uuid.uuid4().hex}.wav"

    with open(filename, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    user_text = speech_to_text(filename)
    intent = detect_intent(user_text)

    conversation.add_user_message(user_text)
    ai_text = get_llm_response(conversation.get(), intent)
    conversation.add_ai_message(ai_text)

    audio_file = text_to_speech(ai_text)

    return {
        "intent": intent,
        "user_text": user_text,
        "ai_text": ai_text,
        "audio_file": audio_file
    }
