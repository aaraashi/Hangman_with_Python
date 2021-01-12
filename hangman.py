"""
Hangman Game with Python inspired by Kylie Ying
Github: https://github.com/aaraashi
"""

import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the list
    while '-' in word or ' ' in word: # words may contain - or space
        word = random.choice(words)

    return word.upper()

def play():
    word = get_valid_word(words)
    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # get user input 
    while len(letters) > 0 and lives > 0:
        print ('You have', lives, ' lives left and you have used these letters: ', ''.join(used_letters))
        drawing = '_________________\n\t|'
        if lives == 6: 
            print(drawing)

         # current word 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        guess = input('Guess a letter: ').upper()
        if guess in alphabet - used_letters: 
            used_letters.add(guess)
            if guess in letters:
             letters.remove(guess)

            else:
                lives = lives -1
                print('\nYour letter,', guess, 'is not in the word.')

                # if lives == 6:
                #     print(drawing + '\n\tO')
                
                if lives == 5:
                    print(drawing + '\n\tO')

                if lives == 4:
                    print(drawing + "\n\tO\n" + "       " + "/")

                if lives == 3:
                    print(drawing + "\n\tO\n" + "       " + "/ \\")

                if lives == 2:
                    print(drawing + "\n\tO\n" + "       " + "/|\\")

                if lives == 1:
                    print(drawing + "\n\tO\n" + "       " + "/|\\\n" + "       " + "/")

        elif guess in used_letters:
            print('You have already used the letter. Please try again.')

        else:
            print('Invalid character. Please try again')


    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
        print(drawing + "\n\tO\n" + "       " + "/|\\\n" + "       " + "/ \\")
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__ == '__main__':
    play()




