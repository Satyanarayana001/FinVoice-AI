import whisper

model = whisper.load_model("base")
result = model.transcribe("20260131-204343.wav")

print("Transcription:")
print(result["text"])
