# CatGod
Tooling for making 'Cat God' video

## Source 
### Hacer's Morse Cat "−•−• •− −"
* https://youtube.com/@Hacer_kun
* https://www.youtube.com/watch?v=8dVQ0813KVM

### Eminem - Rap God
* https://www.youtube.com/watch?v=XbGs_qK2PQA

## Dependencies
* morse-audio-decoder
  * https://pypi.org/project/morse-audio-decoder/
* pysubs2
  * https://pysubs2.readthedocs.io/en/latest/index.html
* python-ffmpeg
* morse-audio-decoder

# What Does This Do?
This will take subtitles formatted in `.srt` and convert them into quantized morse code to concatonate video in time of dots, dashes, and rests for compositing.

# Maybe Just Use MorseAngel
## For my fork
https://github.com/DickyMirrors/morseangel

## OG
https://github.com/f4exb/morseangel

# MP3 to wav
https://superuser.com/questions/675342/convert-mp3-to-wav-using-ffmpeg-for-vbr
`ffmpeg -i song.mp3 -acodec pcm_u8 -ar 22050 song.wav`

# Video to Audio File
https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg

```
ffmpeg -i input.mp4 -map 0:a output.mp3
ffmpeg -i input.mkv -map 0:a output.m4a
ffmpeg -i input.avi -map 0:a -c:a aac output.mka
ffmpeg -i input.mp4 output.wav
```
## Stero to Mono
https://stackoverflow.com/a/51494497
`ffmpeg -i stereo.flac -ac 1 mono.flac`