from playsound import playsound
import os
import datetime
import time
startTime = datetime.datetime(2019,11,29,21,52)
stopTime = datetime.datetime(2019,11,29,21,53)
soundCount = 1

# Audio Played for 1 Minute has Generated 232 samples.
# Playing Audio for 3 Minute can Generate a total 696 samples.
# Audio Length below 1 second

while datetime.datetime.now() < startTime:
    time.sleep(1)
while datetime.datetime.now() >= startTime and datetime.datetime.now() <= stopTime:
    for sounds in os.listdir("testsounds"):
        playsound(os.path.join("testsounds",sounds))
        print(f"Sound Played Count: {soundCount}")
        soundCount = soundCount + 1