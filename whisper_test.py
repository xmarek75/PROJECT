import whisper

model=whisper.load_model("base")

result = model.transcribe("audio_sample.mp3")
print("===============================================================================================")
print(result["text"])