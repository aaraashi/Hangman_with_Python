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

