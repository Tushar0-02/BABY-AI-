from gtts import gTTS
import os


text = "raj is good boy"


tts = gTTS(text=text, lang='en', slow=False)


tts.save("output.mp3")

os.system("start output.mp3") 
