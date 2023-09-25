import ffmpeg
import shutil
import urllib.request

import numpy as np
import scipy.io
import scipy.fft
import scipy.signal
import matplotlib.pyplot as plt

def proccess():
  wav_path = "src/vocals.wav"

  with urllib.request.urlopen(message_url) as response, open(wav_path, "wb") as local_file:
      shutil.copyfileobj(response, local_file)

  samplerate, data = scipy.io.wavfile.read(wave_path)

  time = np.arange(len(data)) / samplerate

  yf = 2.0 / len(data) * np.abs(scipy.fft.fft(data)[:len(data)//2])
  xf = scipy.fft.fftfreq(len(data), 1/samplerate)[:len(data)//2]

  return {
    "time":time, 
    "samplerate":samplerate, 
    "data":data,
    "xf":xf,
    "yf":yf, 
  }
    
def main():
  pass


# Executes the main function
if __name__ == '__main__':
    main()
