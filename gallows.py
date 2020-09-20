from random import *

def new_game():
            print('')
            print('Would you like to play again? (yes/no)')
            answer = input()
            if answer == 'yes':
                return hangman()
            elif answer == 'no':
                print('')
                print('Ok, see you at the gallows next time!')
                return
            else:
                print('')
                print('Just give a yes or no')
                return new_game()

def hangman():
    ls = ['recursive', 'general', 'assembly', 'reticulated', 'python', 'constriction', 'anthropocentricities', 'inconsequentialities','electromagnetically', 'counterculturalisms','crosslinguistically','exhibitionistically','interchangeableness','microelectronically','noninterventionists','phenomenalistically','uncommunicativeness']
    # make a list of words to be used at random in the game
    secret = ls[round((len(ls)-1)*random())]
    # choose a random word
    guess = []
    # empty guess list to add letters to
    display = ''
    for i in secret:
        display += '_ '
    # setting up a display for the secret word
    hangman = [
        ' _____',
        '|',
        '|',
        '|',
        '|',
        '[][][][]'
    ]
    # creating a hangman game display as a list
    count = 0
    # count variable to store wrong guesses

    def make_guesses(secret, guess, display, hangman, count, ls):
        # BASE case to determine if the game
        # has been won or lost
        for i in hangman:
            print(i)
        test = display.split(' ')
        if '_' not in test:
            answer = ''.join(test)
            print('')
            print(answer)
            print('You guessed right! No hanging today.')
            return new_game()
        elif count > 6:
            print('')
            print('Hangman. GG no re.')
            return new_game()
        print('')
        print(display)
        print('')
        print('Make a guess')
        letter = input()[:1]
        if letter in secret:
            for i in range(len(secret)):
                if secret[i] == letter:
                    # print(letter)
                    x = display.split(' ')
                    if x[i] == '_':
                        # print(x[i])
                        x[i] = secret[i]
                        # print(x[i])
                    display = ' '.join(x)               
        else:
            print('The crowd looks on with fervor')
            count += 1
            print(count)
            for i in range(0, len(hangman)):
                if count == 1:
                        if hangman[4] == '|':
                            hangman[4] = '|  /'
                elif count == 2:
                    if hangman[4] == '|  /':
                            hangman[4] = '|  / \\'
                elif count == 3:
                    if hangman[3] == '|':
                            hangman[3] = '|   |'
                elif count == 4:
                    if hangman[3] == '|   |':
                            hangman[3] = '|  /|'
                elif count == 5:
                    if hangman[3] == '|  /|':
                            hangman[3] = '|  /|\\'
                elif count == 6:
                    if hangman[2] == '|':
                            hangman[2] = '|   0';
                elif count == 7:
                    if hangman[2] == '|   0':
                            hangman[1] = '|   |';
                            hangman[5] = '[]    []'
        return make_guesses(secret, guess, display, hangman, count, ls)
    make_guesses(secret, guess, display, hangman, count, ls)
hangman()

