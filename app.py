# app.py
from flask import Flask, render_template, request
import os
from voice_cloning_module import clone_tts

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Render the index.html file
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    # Retrieve the text input from the form
    text = request.form.get('text')
    
    if not text:
        return "Please enter some text.", 400

    # Ensure the directory for audio files exists
    audio_dir = os.path.join('static', 'audio')
    os.makedirs(audio_dir, exist_ok=True)
    
    # Define the output file path
    audio_file_path = os.path.join(audio_dir, 'output.wav')
    
    # Call the voice cloning TTS function to generate the audio file
    clone_tts(text, output_path=audio_file_path)
    
    # Render a template that includes an audio player to play the file
    # The audio URL will be relative to the static folder.
    audio_url = f"/static/audio/output.wav"
    return render_template('result.html', audio_url=audio_url)

if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    app.run(debug=True)