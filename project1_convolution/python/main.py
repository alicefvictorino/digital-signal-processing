import numpy as np
import soundfile as sf
import sounddevice as sd
import os

filename = "Church_Schellingwoude.wav"
new_record = True  # set to False if you want to reuse a previously recorded voice sample
voice_file = "voice.npy"

# Load the stereo audio file; y is a 2D array (samples x channels)
y, Fs = sf.read(filename)

impulse_response = y[:, 0]

if new_record:
    duration = 7  # seconds
    print(f"Recording voice for {duration} seconds...")
    y_recorded = sd.rec(int(duration * Fs), samplerate=Fs, channels=1)
    sd.wait()  
    y_recorded = y_recorded.flatten()  # convert to 1D array
    # Save the recording for reuse
    np.save(voice_file, y_recorded)
else:
    # Load a previously recorded voice sample
    if os.path.exists(voice_file):
        y_recorded = np.load(voice_file)
    else:
        raise FileNotFoundError(f"No recorded voice found at {voice_file}. Set new_record=True to record.")

# Perform convolution between the impulse response and the recorded voice
y_conv = np.convolve(impulse_response, y_recorded)
y_conv_normalized = y_conv / np.max(np.abs(y_conv))

sf.write("results.wav", y_conv_normalized, Fs)

sd.play(y_conv_normalized, Fs)
sd.wait()
