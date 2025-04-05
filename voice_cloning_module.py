# voice_cloning_module.py
import sys
sys.path.append("/Users/ashwinbijoy/Desktop/folder/code/Real-Time-Voice-Cloning")

import numpy as np
import soundfile as sf
import librosa

# Import the TTS modules from the Real-Time Voice Cloning toolkit
from encoder import inference as encoder_module
from synthesizer.inference import Synthesizer
from vocoder import inference as vocoder_module

def load_models():
    """
    Loads the pretrained models for the encoder, synthesizer, and vocoder.
    Make sure to adjust the paths according to your setup.
    """
    # Load the encoder model
    encoder_module.load_model("encoder/saved_models/pretrained.pt")
    
    # Load the synthesizer model
    synthesizer = Synthesizer("synthesizer/saved_models/pretrained/pretrained.pt")
    
    # Load the vocoder model
    vocoder_module.load_model("vocoder/saved_models/pretrained/pretrained.pt")
    
    return encoder_module, synthesizer, vocoder_module

def clone_tts(text, voice_sample_path, output_path, encoder, synthesizer, vocoder):
    """
    Clones your voice and synthesizes speech for the given text.
    
    Steps:
      1. Preprocess the voice sample and extract an embedding.
      2. Generate a mel spectrogram from the input text conditioned on the voice embedding.
      3. Convert the spectrogram to a waveform using the vocoder.
      4. Save the generated waveform as a WAV file.
    
    Parameters:
      text (str): The text input to be synthesized.
      voice_sample_path (str): Path to your voice sample.
      output_path (str): Path where the output WAV file will be saved.
      encoder: Loaded encoder module.
      synthesizer: Loaded synthesizer instance.
      vocoder: Loaded vocoder module.
    """
    # 1. Preprocess the voice sample and compute the embedding
    wav, _ = librosa.load(voice_sample_path, sr=16000)
    wav = encoder.preprocess_wav(wav)
    embed = encoder.embed_utterance(wav)
    
    # 2. Synthesize a mel spectrogram from the text and the voice embedding
    texts = [text]
    embeds = [embed]
    specs = synthesizer.synthesize_spectrograms(texts, embeds)
    spec = specs[0]
    
    # 3. Generate the waveform from the spectrogram using the vocoder
    generated_wav = vocoder.infer_waveform(spec)
    
    # Optional: Post-process the waveform (e.g., trimming silence, normalization)
    generated_wav = np.pad(generated_wav, (0, synthesizer.sample_rate), mode="constant")
    
    # 4. Save the waveform as a WAV file
    sf.write(output_path, generated_wav, synthesizer.sample_rate)
    
    return output_path