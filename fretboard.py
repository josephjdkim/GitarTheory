import numpy as np
import metronome as mt
import sys
import time

sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

def frets(scale):
    invalid_inp = 0
    if scale == 'sharp':
        perm = np.random.permutation(sharp)
    elif scale == 'flat':
        perm = np.random.permutation(flat)
    elif scale == 'both':
        perm = np.random.permutation(flat + sharp)
    else:
        print('Please use the keywords "sharp", "flat", or "both".')
        invalid_inp = 1

    if not invalid_inp:
        # if user would like a metronome
        print('Would you like to use a metronome? (y/n):')
        met = input('>> ').lower()
        while met != 'y' and met != 'n':
            print('Would you like to use a metronome? (y/n):')
            met = input('>> ').lower()
        if met == 'y':
            print('BPM?:')
            bpm = int(input('>> '))

        print()
        for n in perm:
            print(n)
            if met == 'y':
                mt.metronome(bpm) # displays metronome if user asked for one

        sys.stdout.flush()
        sys.stdout.write(' ') # clears final beat on std.out

def keys(scale):
    print()