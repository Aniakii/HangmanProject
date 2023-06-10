from random import randint

def get_word():
    try:
        with open("words_base.txt", 'r', encoding="utf-8") as file:
            words = file.readlines()
            random_number = randint(0, len(words)-1)
            word = words[random_number]
            encrypted_word = len(word) * "_"
            return word, encrypted_word
    except FileNotFoundError:
        ...


def guess_letter(letter, word_to_guess, guessed_letters):
    if len(letter) == 0:
        return False
    if len(letter) > 1:
        if letter == word_to_guess:
            return True
        else:
            return False
    if letter.lower() in word_to_guess.lower() and letter not in guessed_letters:
        positions_of_letters = []
        for position, let in enumerate(word_to_guess, start=0):
            if let.lower() == letter.lower():
                positions_of_letters.append(position)
        return True, positions_of_letters
    else:
        return False