import librosa
import numpy as np
import matplotlib.pyplot as plt
import random
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image


def select_file():
    file_path = filedialog.askopenfilename()
    file_label.config(text="Selected File: " + file_path)
    return file_path

def create_spectrogram():
    # get the selected file path
    file_path = select_file()
    print(f"Loading audio file: {file_path}")

    # load the audio file
    y, sr = librosa.load(file_path)

    print(f"Audio data shape: {y.shape}, sample rate: {sr}")
    if y.size == 0:
        print("Audio data is empty!")
        exit()

    # calculate the spectrogram
    S = np.abs(librosa.stft(y))

    # convert to decibels
    S_db = librosa.amplitude_to_db(S, ref=np.max)

    # create the colormap
    cmaps = ['Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c']
    cmap_cor = random.choice(cmaps)
    cmap = plt.get_cmap(cmap_cor)

    # plot and save the spectrogram
    fig = plt.subplots(figsize=(10, 6))
    plt.axis('off')
    plt.imshow(librosa.power_to_db(S, ref=np.max), cmap=cmap, aspect='auto', origin='lower')
    plt.savefig('espectrograma.png')
    print("Spectrogram saved to file!")

    img = ImageTk.PhotoImage(Image.open('espectrograma.png'))
    panel.configure(image=img)
    panel.image = img

# create the GUI
root = tk.Tk()
root.title("File Input Example")

file_label = tk.Label(root, text="No file selected")
file_label.pack(pady=10)
file_button = tk.Button(root, text="Select File", command=create_spectrogram)
file_button.pack()

panel = tk.Label(root)
panel.pack(pady=10)

root.mainloop()




