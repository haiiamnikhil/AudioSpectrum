import sounddevice as sd
from scipy.io import wavfile
import os as os

try:
    os.mkdir("Recordings")
except FileExistsError:
    pass

FramesperSec = 44100
RecDur = 1
count = 0
recount = 0
while count <= 500:
    recordAudio = sd.rec((RecDur * FramesperSec),samplerate=FramesperSec,channels=2)
    sd.wait()
    wavfile.write(os.path.join("Recordings",f"recorded {recount}.wav"),FramesperSec,recordAudio)
    recount = recount + 1
    count = count + 1