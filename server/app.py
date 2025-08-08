from flask import Flask, request, send_file
from stt import transcribe
from model import get_response
from server.tts import synthesize
import tempfile

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return "No file part", 400

    audio_file = request.files['file']
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        audio_file.save(temp_audio.name)
        temp_audio_path = temp_audio.name

    text = transcribe(temp_audio_path)
    response_text = get_response(text)
    response_audio_path = synthesize(response_text)

    return send_file(response_audio_path, mimetype="audio/wav")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
