from flask import Flask, render_template, request, send_file
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

    # Call the voice cloning TTS function to generate the audio file
    audio_file_path = clone_tts(text)
    
    # Return the generated audio file for download or playback
    return send_file(audio_file_path, as_attachment=True)

if __name__ == '__main__':
    # Run the Flask app in debug mode for development
    app.run(debug=True)