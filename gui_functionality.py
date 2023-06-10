from game_mechanism import get_word, guess_letter
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

word_to_guess = ""
encrypted_word = ""
mistakes_left = 13
guessed_letters = []

def start_game(word_browser, mistakes_browser):
    global word_to_guess, encrypted_word, guessed_letters, mistakes_left

    word_to_guess, encrypted_word = get_word()
    guessed_letters = []
    mistakes_left = 13
    display_word(encrypted_word, word_browser)
    display_mistakes(mistakes_browser)

def display_word(word, word_browser):
    word_to_display = ' '.join(char for char in word)
    word_browser.clear()
    word_browser.append(word_to_display)
    
def display_mistakes(mistakes_browser):
    mistakes_browser.clear()
    mistakes_browser.append(str(mistakes_left))

def show_picture(hangman_view):

    hangman_view.setPixmap(QPixmap(f"hangman_pictures/hangman{13-mistakes_left}.png"))

def get_guessed_letter(write_letter,hangman_view,mistakes_browser,word_browser):
    global mistakes_left, encrypted_word, guessed_letters

    written_letter = write_letter.toPlainText()
    if written_letter == "":
        QMessageBox.critical(write_letter, "NIE PODANO LITERY", "Musisz wpisać literę, aby spróbować odgadnąć hasło")
    else:
        result = guess_letter(written_letter,word_to_guess,guessed_letters)
        if isinstance(result, bool):
            if result:
                display_word(word_to_guess, word_browser)
                QMessageBox.critical(word_browser, "KONIEC GRY", "Brawo, udało Ci się odgadnąć hasło!!!")
            else:
                mistakes_left -= 1
                show_picture(hangman_view)
                display_mistakes(mistakes_browser)
                if mistakes_left == 0:
                    QMessageBox.critical(mistakes_browser, "KONIEC GRY", f"Niestety, nie udało ci się odgadnąć słowa :(\nSłowo, które należało odgadnąć to: {word_to_guess}")
                    start_game(word_browser,mistakes_browser)
        else:
            positions = result[1]
            for position in positions:
                letter = word_to_guess[position]
                encrypted_word = encrypted_word[:position] + letter + encrypted_word[position + 1:]
            display_word(encrypted_word,word_browser)



