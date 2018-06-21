import chords as ch
import scales as sc

VERSION = '0.2.0'

def border():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def intro_prompt():
    border()
    print('Welcome to GitarTheory version ' + VERSION + '!\n'
        'This app was made for the beginner-guitarist.\n\n'
        'Enter "scales" or "chords" to get started, or '
        'enter "help" for a more\ndetailed list of commands.')

def state_check(state):
    if state == 'home':
        home()
        return 0
    if state == 'chords':
        chords()
        return 0

def help(state):
    print('HELP FILLER')
    state_check(state)

def chords():
    state = 'chords'
    border()
    print("Enter a guitar chord to find out its construction.")
    user_inp = input(">> ")
    if user_inp == 'help':
        help(chords)
    elif user_inp == 'formatting':
        ch.formatting()
    elif user_inp == 'qualities':
        ch.qualitieshelp()
    elif user_inp == 'back':
        state = 'home'
    elif ch.chord_comps(user_inp)[0] not in ch.notenum or ch.chord_comps(user_inp)[1] not in ch.quality:
        ch.incorrectinp()
    else:
        chordOut, qualityOut = (ch.chord_create(ch.chord_comps(user_inp)))
        print(chordOut)
        print(qualityOut)
    state_check(state)

def home():
    border()
    print('Main menu:')
    user_inp = input('>> ')
    user_inp = user_inp.lower()

    if user_inp == 'help':
        help('home')
    elif user_inp == 'chords':
        chords()
    elif user_inp == 'scales':
        scales()

def main():
    intro_prompt()
    home()

main()