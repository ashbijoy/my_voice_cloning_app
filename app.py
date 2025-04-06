# app.py
# http://127.0.0.1:5000

from flask import Flask, render_template, request
import os
from voice_cloning_module import clone_tts, load_models

app = Flask(__name__)

# Load models once when the app starts
encoder, synthesizer, vocoder = load_models()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form.get('text')
    if not text:
        return "Please enter some text.", 400

    # Ensure that the audio output directory exists
    audio_dir = os.path.join('static', 'audio')
    os.makedirs(audio_dir, exist_ok=True)
    
    # Define the output file path
    audio_file_path = os.path.join(audio_dir, 'output.wav')
    
    # Generate the cloned voice audio using the full TTS pipeline
    clone_tts(text, voice_sample_path="samples/my_voice.wav", output_path=audio_file_path,
              encoder=encoder, synthesizer=synthesizer, vocoder=vocoder)
    
    # Prepare the URL for the audio file relative to the static folder
    audio_url = f"/static/audio/output.wav"
    return render_template('result.html', audio_url=audio_url)

if __name__ == '__main__':
    app.run(debug=True)