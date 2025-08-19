import matplotlib.pyplot as plt
from scipy.io import wavfile

def plot_audio(filename, channel=0):
    Fs, data = wavfile.read(filename)
    
    if len(data.shape) > 1:
        audio = data[:, channel]
    else:
        audio = data
    
    t = [i/Fs for i in range(len(audio))]
    
    plt.figure(figsize=(12,4))
    plt.plot(t, audio)
    plt.title(f'Áudio: {filename} (Canal {channel})')
    plt.xlabel('Tempo [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

plot_audio('Church_Schellingwoude.wav')