import pysubs2
import time
import numpy as np
import simpleaudio as sa
import ffmpeg
import shutil
import urllib.request

import numpy as np
import scipy.io
import scipy.fft
import scipy.signal
import matplotlib.pyplot as plt

rip = True
play = True

leading = 0.001
spacing = 0.01

dot = 0.025
dot_freq = 500
dash = 0.05
dash_freq = dot_freq-25

morse_subtitles_file = "build/CatGod.ass"
rapgod_subtitles_file = "./src/rapgod/Meowminem-CatGod.srt"

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

def sound(x,z):
	frequency = x # Our played note will be 440 Hz
	fs = 44100  # 44100 samples per second
	seconds = z  # Note duration of 3 seconds	

	# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
	t = np.linspace(0, seconds, int(seconds * fs), False)	
	#t = np.arange(0, 0.2, 0.2 * fs)	
	
	# Generate a 440 Hz sine wave
	note = np.sin(frequency * t * 2 * np.pi)
	
	# Ensure that highest value is in 16-bit range
	audio = note * (2**15 - 1) / np.max(np.abs(note))

	# Convert to 16-bit data
	audio = audio.astype(np.int16)	
	
	if play:
		# Start playback
		play_obj = sa.play_buffer(audio, 1, 2, fs)	

		# Wait for playback to finish before exiting
		play_obj.wait_done()

	return audio

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ',':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-', '"':'.-..-.',
					"'": '.----.', '\\': '\n', '!':'-·-·--',
					'♪':'♪'}

def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':
			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += ' '
	return cipher

def decrypt(message):
	message += ' '
	decipher = ''
	citext = ''
	for letter in message:
		if (letter != ' '):
			i = 0
			citext += letter
		else:
			i += 1
			if i == 2 :
				decipher += ' '
			else:
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher

def play_dot():
    return sound(dot_freq,dot)

def play_dash():
    return sound(dash_freq,dash) 

def play_char(ch):
	if ch == ' ':
		time.sleep(spacing)
		return spacing

	morseval = MORSE_CODE_DICT[ch]
	morse = []
	for d in morseval:
		if d == '.':
			morse.append(play_dot())
			time.sleep(leading)
		else:
			morse.append(play_dash())
			time.sleep(leading)
	return morse, leading
	
def txt2morse(txt):
	print(txt)
	for ch in txt.upper():    
		play_char(ch),  

def main():
	#import pdb; pdb.set_trace()
	if rip:
		subs = pysubs2.load(rapgod_subtitles_file, encoding="utf-8")
		for line in subs:
			txt = encrypt(line.text.upper())
			line.text = "{\\be1}" + txt
		subs.save(morse_subtitles_file)

	subs = pysubs2.load(morse_subtitles_file, encoding="utf-8")
	for line in subs:
		txt = decrypt(line.text.strip('♪').strip().strip("{\\be1}"))
		txt2morse(txt.strip('♪ '))

if __name__ == '__main__':
	main()
