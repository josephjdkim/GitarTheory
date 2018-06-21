import chords as ch
import keys as ke
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
    if state == 'scales_prompt':
        scales_prompt()
        return 0

# help command takes state so that user can be returned to proper menu after
def help(state):
    print(''
        '"help" lists commands.\n'
        '"back" returns you to the previous level of the program.'
        '')
    state_check(state)

# chord construction/knowledge database
# program goes here if user selects 'chords' at main menu
def chords():
    state = 'chords'
    border()
    print('Main menu: Chords:')
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
    elif user_inp == 'quit':
        return 0
    elif ch.chord_comps(user_inp)[0] not in ch.notenum or ch.chord_comps(user_inp)[1] not in ch.quality:
        ch.incorrectinp()
    else:
        chordOut, qualityOut = (ch.chord_create(ch.chord_comps(user_inp)))
        print(chordOut)
        print(qualityOut)
    state_check(state)

# program goes here if user chooses 'keys' at scales menu
def scales_keys():
    state = 'scales_keys'
    border()
    print('What major key would you like to look at?')
    user_inp = input('>> ')
    ke.keys(user_inp)

# program goes here is user chooses 'frets' at scales menu
def scales_frets():
    state = 'scales_frets'
    border()
    print('Would you like to look at sharps, flats, or both?')
    user_inp = input('>> ').lower()
    fb.frets(user_inp)

# program goes here if user selects 'scales' at main menu
def scales_prompt():
    state = 'scales_prompt'
    border()
    print('Main menu: Scales:')
    print('Would you like to practice scales of certain keys, or '
        'would you like\nto practice memorizing the fretboard? (keys/frets)')
    
    user_inp = input('>> ').lower()
    
    if user_inp == 'keys':
        scales_keys()
    elif user_inp == 'frets':
        scales_frets()
    elif user_inp == 'back':
        state = 'home'
    elif user_inp == 'quit':
        return 0
    else:
        print('Invalid input. Choose "keys" or "frets".')
    state_check(state)

# main menu
def home():
    border()
    print('Main menu:')
    print('Would you like to practice scales or learn chords? (scales/chords)')
    user_inp = input('>> ').lower()

    if user_inp == 'chords':
        chords()
    elif user_inp == 'scales':
        scales_prompt()
    elif user_inp == 'help':
        help('home')
    elif user_inp == 'quit':
        return 0
    else:
        print('Invalid input. Type "help" for a list of commands.')
        home()

def main():
    intro_prompt()
    home()

main()