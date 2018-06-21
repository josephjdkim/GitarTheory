import chords as ch
import fretboard as fb

VERSION = '0.2.0'

# border that is printed between each action
def border():
    print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# greeting message
def intro_prompt():
    border()
    print('Welcome to GitarTheory version ' + VERSION + '!\n'
        'This app was made for the beginner-guitarist.\n\n'
        'Enter "scales" or "chords" to get started, or '
        'enter "help" for a more\ndetailed list of commands.')

# checks states for redirection or returning to proper menu
def state_check(state):
    if state == 'home':
        home()
        return 0
    if state == 'chords':
        chords()
        return 0
    if state == 'scales':
        scales()
        return 0

# help command takes state so that user can be returned to proper menu after
def help(state):
    print('HELP FILLER')
    state_check(state)

# chord construction/knowledge database
# program goes here if user selects 'chords' at main menu
def chords():
    state = 'chords'
    border()
    print('Enter a guitar chord to find out its construction.')
    user_inp = input('>> ')
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

def scales_keys():
    print('rip')

def scales_frets():
    print('non-rip')

# program goes here if user selects 'scales' at main menu
def scales_prompt():
    state = 'scales_prompt'
    border()
    print('Would you like to practice scales of certain keys, or '
        'would you like\nto practice memorizing the fretboard?')
    
    user_inp = input('>> ').lower()
    
    if user_inp == 'keys':
        scales_keys()
    elif user_inp == 'frets':
        scales_frets()

# main menu
def home():
    border()
    print('Main menu:')
    user_inp = input('>> ').lower()

    if user_inp == 'help':
        help('home')
    elif user_inp == 'chords':
        chords()
    elif user_inp == 'scales':
        scales_prompt()

def main():
    intro_prompt()
    home()

main()