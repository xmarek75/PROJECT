import whisper

# Načtení modelu
model = whisper.load_model("base")

# Transkripce souboru
result = model.transcribe("audio_sample.mp3")


def simple_hours(seconds: float) -> float:
    minutes = seconds // 60  # Celé minuty
    seconds = seconds % 60     # Zbytek sekund
    return minutes, seconds
# Výpis transkripce s časovými značkami
print("===============================================================================================")
for segment in result["segments"]:
    start_time = segment["start"]  # Čas začátku segmentu
    end_time = segment["end"]      # Čas konce segmentu
    text = segment["text"]         # Text segmentu
    start_minutes, start_seconds = simple_hours(start_time)#prepis na minuty a vteriny
    end_minutes, end_seconds = simple_hours(end_time)

    print(f"[{start_minutes:.0f}:{start_seconds:.2f} - {end_minutes:.0f}:{end_seconds:.2f}] {text}")
