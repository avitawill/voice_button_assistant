import RPi.GPIO as GPIO
import time
import requests
from config import BUTTON_PIN, LED_PIN, SERVER_URL, RECORD_SECONDS
from record import record_audio
from play_audio import play_audio

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

def button_callback(channel):
    GPIO.output(LED_PIN, GPIO.HIGH)
    audio_file = record_audio(RECORD_SECONDS)
    
    with open(audio_file, 'rb') as f:
        files = {'file': f}
        response = requests.post(SERVER_URL, files=files)
    
    with open('/tmp/response.wav', 'wb') as out:
        out.write(response.content)
    
    play_audio('/tmp/response.wav')
    GPIO.output(LED_PIN, GPIO.LOW)

GPIO.add_event_detect(BUTTON_PIN, GPIO.RISING, callback=button_callback, bouncetime=500)

print("Ready. Press the button.")
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
