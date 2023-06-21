from random import randint
from enum import Enum
words = []
easy_words = []
medium_words = []
hard_words = []

class Level(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    RANDOM = 0

def load_words():
    global words, easy_words, medium_words, hard_words
    try:
        with open("words_base.txt", 'r', encoding="utf-8") as file:
            words = file.readlines()
            words = [word.rstrip() for word in words]
            for word in words:
                if len(word) < 6:
                    easy_words.append(word)
                elif len(word) < 11:
                    medium_words.append(word)
                else:
                    hard_words.append(word)
            return words, easy_words, medium_words, hard_words
    except FileNotFoundError:
        ...

def get_word(level):
    global words, easy_words, medium_words, hard_words
    word = ""
    if level == Level.EASY.value:
        if len(easy_words) > 0:
            random_number = randint(0, len(easy_words)-1)
            word = easy_words[random_number]
    elif level == Level.MEDIUM.value:
        if len(medium_words) > 0:
            random_number = randint(0, len(medium_words)-1)
            word = medium_words[random_number]
    elif level == Level.HARD.value:
        if len(hard_words) > 0:
            random_number = randint(0, len(hard_words)-1)
            word = hard_words[random_number]
    elif level == Level.RANDOM.value:
        random_number = randint(0, len(words)-1)
        word = words[random_number]
    encrypted_word = (len(word)) * "_"
    return word, encrypted_word


def guess_letter(letter, word_to_guess, guessed_letters):
    whole_word = True
    if len(letter) == 0:
        return False
    elif letter.lower() in word_to_guess.lower() and letter not in guessed_letters:
        positions_of_letters = []
        guessed_letters.append(letter)
        for position, let in enumerate(word_to_guess, start=0):
            if let.lower() == letter.lower():
                positions_of_letters.append(position)
        return True, positions_of_letters
    else:
        return False
    