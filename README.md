## vue.js

## python.py

## openai - whisper

## FastApi

### zprovozneni whisperu, lokalne

><b>instalace ffmpeg</b><br>
`sudo apt install ffmpeg`

><b>Instalace pip</b><br>
`sudo apt install python3-pip`

><b>vytvoreni virtualniho prostredi</b><br>
`python3 -m venv venv`

><b>spusteni virtualniho prostredi</b><br>
`source venv/bin/activate`

><b>Instalace OpenAI Whisper</b><br>
`pip install git+https://github.com/openai/whisper.git`<br>
`pip install whisper`

<b>kod pro spusteni whisperu v python</b><br>
```
import whisper

model=whisper.load_model("base")

result = model.transcribe("audio_sample.mp3")
print(result["text"])
```



------------------------------------

