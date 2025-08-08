import sounddevice as sd
import numpy as np
import wave
import tempfile

def record_audio(seconds=5, samplerate=16000):
    print("Recording...")
    audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    with wave.open(temp_file.name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    
    print("Saved to", temp_file.name)
    return temp_file.name

