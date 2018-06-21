import numpy as np
import metronome as mt
import sys
import time

sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

def frets(scale):
    if scale.lower() == 'sharp':
        perm = np.random.permutation(sharp)
    elif scale.lower() == 'flat':
        perm = np.random.permutation(flat)
    elif scale.lower() == 'both':
        perm = np.random.permutation(flat+sharp)
    elif scale.lower() == 'quit' or scale.lower() == 'q':
        print()
        return 99
    else:
        print('Please use the keywords "sharp", "flat", "both", or "quit".\n')
        return 0

    met = input("Would you like to use a metronome? (y/n): ")
    while met.lower() != 'y' and met.lower() != 'n':
        met = input("Would you like to use a metronome? (y/n): ")
    if met == 'y':
        bpm = int(input('BPM?: '))

    print()
    for n in perm:
        print(n)
        if met == 'y':
            mt.metronome(bpm) # displays metronome if user asked for one

    sys.stdout.flush()
    sys.stdout.write(' ') # clears final beat on std.out

    print()

def keys(scale):
    print()