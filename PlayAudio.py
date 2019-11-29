from playsound import playsound
import os
import pytz

RepeatSounds = 0
time = pytz.timezone("")

while RepeatSounds <= 500:
    for sounds in os.listdir("testsounds"):
        playsound(os.path.join("testsounds",sounds))
        RepeatSounds = RepeatSounds + 1