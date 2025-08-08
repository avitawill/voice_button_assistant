from gtts import gTTS
import tempfile

def synthesize(text):
    tts = gTTS(text, lang='he')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name
