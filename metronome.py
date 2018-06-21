import time
import sys

def metronome(bpm):
    spb = (1/bpm)*60 # calculate seconds per beat
    def tracker():
        while True:
            for beat in range(2, 5):
                yield str(beat)
    metr = tracker()
    time.sleep(spb)
    for _ in range(3):
        sys.stdout.write(next(metr)) # display beat number
        sys.stdout.flush()
        time.sleep(spb) # delay based on bpm
        sys.stdout.write('\b') # clear