import metronome as mt
import sys
import time

key_Gs = ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']
key_Ab = ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G']
key_A = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
# below needs to be taken care of
key_As = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_Bb = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_B = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_C = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_Cs = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_Db = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_D = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_Ds = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_Eb = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_E = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_F = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_Fs = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_Gb = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_G = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']


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