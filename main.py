import pysubs2
from morse import encrypt, decrypt
import ffmpeg
from morse_audio_decoder.morse import MorseCode

# pysub2 for transcript parsing
# https://pysubs2.readthedocs.io/en/latest/index.html
def subload():
  subs = pysubs2.load("my_subtitles.ass", encoding="utf-8")
  subs.shift(s=2.5)
  for line in subs:
      line.text = "{\\be1}" + line.text
  subs.save("my_subtitles_edited.ass")

# ffmpeg concat
# https://www.reddit.com/r/learnpython/comments/rbr32l/combine_list_of_video_into_single_video/ilre0ia/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
def video_stitch():
  # list of video files
  files = []

  # eparate video and audio, then flat the array
  video_and_audios_files = [item for sublist in map(lambda f: [f.video, f.audio], files) for item in sublist]

  # concat all
  joined = (
      ffmpeg
        .concat(*video_and_audios_files, v=1, a=1)
        .node
    )

  # merge video and audio
  (
    ffmpeg
      .output(joined[0], joined[1], 'out.mp4')
      .run()
  )

# morse-audio-decoder
# https://pypi.org/project/morse-audio-decoder/
morse_code = MorseCode.from_wavfile("/path/to/file.wav")
out = morse_code.decode()
print(out)
  
# Text morse code converter
# https://www.geeksforgeeks.org/morse-code-translator-python/
# Hard-coded driver function to run the program
def main():
    message = "GEEKS-FOR-GEEKS"
    result = encrypt(message.upper())
    print (result)
 
    message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
    result = decrypt(message)
    print (result)
 
# Executes the main function
if __name__ == '__main__':
    main()
