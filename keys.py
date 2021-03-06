import metronome as mt
import sys
import time

key_Gs = ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']
key_Ab = ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G']
key_A = ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#']
key_As = ['A#', 'C', 'D', 'D#', 'F', 'G', 'A']
key_Bb = ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A']
key_B = ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#']
key_C = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
key_Cs = ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']
key_Db = ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C']
key_D = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']
key_Ds = ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D']
key_Eb = ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D']
key_E = ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#']
key_F = ['F', 'G', 'A', 'A#', 'C', 'D', 'E']
key_Fs = ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F']
key_Gb = ['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F']
key_G = ['G', 'A', 'B', 'C', 'D', 'E', 'F#']

def keys(key):
    invalid_inp = 0
    # major keys (DJ KHALED)
    # i need to make this a dictionary...
    key = key.lower()
    if key == 'g#':
        perm = key_Gs
    elif key == 'ab':
        perm = key_Ab
    elif key == 'a':
        perm = key_A
    elif key == 'a#':
        perm = key_As
    elif key == 'bb':
        perm = key_Bb
    elif key == 'b':
        perm = key_B
    elif key == 'c':
        perm = key_C
    elif key == 'c#':
        perm = key_Cs
    elif key == 'db':
        perm = key_Db
    elif key == 'd':
        perm = key_D
    elif key == 'd#':
        perm = key_Ds
    elif key == 'eb':
        perm = key_Eb
    elif key == 'f':
        perm = key_F
    elif key == 'f#':
        perm = key_Fs
    elif key == 'gb':
        perm = key_Gb
    elif key == 'g':
        perm = key_G
    else:
        print('Please enter a key (like C, Ab, or G#)".')
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