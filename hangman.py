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

    # get user input 
    while len(letters) > 0:
        print ('You have used these letters: ', ''.join(used_letters))

        guess = input('Guess a letter: ').upper()
        if guess in alphabet - used_letters: 
            used_letters.add(guess)
            if guess in letters:
             letters.remove(guess)
        
        elif guess in used_letters:
            print('You have already used the letter. Please try again.')

        else:
            print('Invalid character. Please try again')


if __name__ == '__main__':
    play()




