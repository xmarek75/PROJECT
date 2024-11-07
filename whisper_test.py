import whisper
from faster_whisper import WhisperModel
# Velikost modelu
model_size = "large-v3"
# Načtení modelu
#model = whisper.load_model("base") #pro normalni whisper
model = WhisperModel(model_size, device="cpu", compute_type="int8") #pro faster-whisper
# Transkripce souboru
# # # # result = model.transcribe("audio_sample.mp3")


# # # # def simple_hours(seconds: float) -> float:
# # # #     minutes = seconds // 60  # Celé minuty
# # # #     seconds = seconds % 60     # Zbytek sekund
# # # #     return minutes, seconds
# # # # # Výpis transkripce s časovými značkami
# # # # for segment in result["segments"]:
# # # #     start_time = segment["start"]  # Čas začátku segmentu
# # # #     end_time = segment["end"]      # Čas konce segmentu
# # # #     text = segment["text"]         # Text segmentu
# # # #     start_minutes, start_seconds = simple_hours(start_time)#prepis na minuty a vteriny
# # # #     end_minutes, end_seconds = simple_hours(end_time)

    
# # # #     #new_string = str(start_minutes)+":"+str(start_seconds) +"-"+ str(end_minutes)+":"+str(end_seconds) + text
# # # #     new_string = f"[{start_minutes:.0f}:{start_seconds:.0f} - {end_minutes:.0f}:{end_seconds:.0f}] {text}"
# # # #     #print(f"[{start_minutes:.0f}:{start_seconds:.0f} - {end_minutes:.0f}:{end_seconds:.0f}] {text}")
# # # #     print(new_string)

segments, info = model.transcribe("video_sample.mp4", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
