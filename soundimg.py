import librosa
import librosa.display
import matplotlib.pyplot as plt

# Carrega o arquivo de som
filename = 'exemplo.wav'
y, sr = librosa.load(filename)

# Calcula o espectrograma
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
plt.figure(figsize=(10, 5))
librosa.display.specshow(D, y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma')
plt.xlabel('Tempo')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()
