from game_mechanism import get_word, guess_letter, load_words
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QAbstractItemView
from PyQt5.QtCore import QStringListModel

word_to_guess = ""
encrypted_word = ""
mistakes_left = 13
level = 0
guessed_letters = []
all_words = []
easy_words = []
medium_words = []
hard_words = []
polish_letters = "ĄąĆćĘęŹźŻżŁłÓóŚś"

def open_different_window(First_Window, Second_Window):
    First_Window.hide()
    Second_Window.show()

def start_game(word_browser, mistakes_browser, hangman_view, Menu_Window, Game_Window,chosen_level=None):
    global word_to_guess, encrypted_word, guessed_letters, mistakes_left, all_words, level

    if chosen_level is None:
        chosen_level = level
    if len(all_words) == 0:
        get_all_words()
    word_to_guess, encrypted_word = get_word(chosen_level)
    if word_to_guess == "":
        QMessageBox.critical(word_browser, "BRAK SŁOWA", "W bazie nie ma żadnego słowa, które odpowiadałoby wybranemu poziomowi")
    else:
        guessed_letters = []
        mistakes_left = 13
        level = chosen_level
        display_word(encrypted_word, word_browser)
        display_mistakes(mistakes_browser)
        show_picture(hangman_view)
        open_different_window(Menu_Window, Game_Window)

def get_all_words() -> list[str]:
    global all_words, easy_words, medium_words, hard_words
    all_words, easy_words, medium_words, hard_words = load_words()
    return all_words

def display_word(word, word_browser):
    word_to_display = ' '.join(char for char in word)
    word_browser.clear()
    word_browser.append(word_to_display)
    
def display_mistakes(mistakes_browser):
    mistakes_browser.clear()
    if mistakes_left <= 5:
        mistakes_browser.append(f"<font color='red'>{str(mistakes_left)}</font>")
    else:
        mistakes_browser.append(str(mistakes_left))

def show_picture(hangman_view):

    hangman_view.setPixmap(QPixmap(f"hangman_pictures/hangman{13-mistakes_left}.png"))

def get_guessed_letter(write_letter,hangman_view,mistakes_browser,word_browser):
    global mistakes_left, encrypted_word, guessed_letters

    written_letter = write_letter.toPlainText()
    if written_letter == "":
        QMessageBox.critical(write_letter, "NIE PODANO LITERY", "Musisz wpisać literę, aby spróbować odgadnąć hasło.")
    elif written_letter in guessed_letters:
        QMessageBox.critical(write_letter, "POWTÓRZONA LITERA", "Wpisana litera była już wcześniej podana.")
    elif written_letter.lower() == word_to_guess.lower():
        display_word(written_letter, word_browser)
        message = QMessageBox(QMessageBox.Information,"KONIEC GRY","Brawo, udało Ci się odgadnąć hasło!!!")
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
    else:
        result = guess_letter(written_letter,word_to_guess,guessed_letters)
        if isinstance(result, bool):
            if result:
                display_word(word_to_guess, word_browser)
                message = QMessageBox(QMessageBox.Information,"KONIEC GRY","Brawo, udało Ci się odgadnąć hasło!!!")
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
            else:
                mistakes_left -= 1
                show_picture(hangman_view)
                display_mistakes(mistakes_browser)
                if mistakes_left == 0:
                    QMessageBox.critical(mistakes_browser, "KONIEC GRY", f"Niestety, nie udało ci się odgadnąć słowa :(\nSłowo, które należało odgadnąć to: {word_to_guess}")
        else:
            positions = result[1]
            for position in positions:
                letter = word_to_guess[position]
                encrypted_word = encrypted_word[:position] + letter + encrypted_word[position + 1:]
            display_word(encrypted_word,word_browser)
            test = encrypted_word.replace(" ", "")
            if test.lower() == word_to_guess.lower():
                message = QMessageBox(QMessageBox.Information,"KONIEC GRY","Brawo, udało Ci się odgadnąć hasło!!!")
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
    write_letter.clear()

def setup_list_view(words_list_view, scroll_widget):
    global all_words

    if words_list_view.model() is None:
        model = QStringListModel()
        words_list_view.setModel(model)
        if len(all_words) == 0:
            all_words = get_all_words()
    else:
        model = words_list_view.model()
    
    model.setStringList(all_words)
    scroll_widget.setMaximum(model.rowCount() - 1)

    def scroll_to_index(scroll_index):
        if scroll_widget.signalsBlocked():
            return
                
        model_index = model.index(scroll_index)
        words_list_view.scrollTo(model_index, QAbstractItemView.PositionAtCenter)
                
        scroll_widget.blockSignals(True)
        scroll_widget.setValue(scroll_index)
        scroll_widget.blockSignals(False)

    scroll_widget.valueChanged.connect(scroll_to_index)

    words_list_view.setSelectionMode(QAbstractItemView.NoSelection)
    words_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

    words_list_view.setVerticalScrollBar(scroll_widget)

def add_word(write_word,words_list_view, scroll_widget):
    global all_words, easy_words, medium_words, hard_words
    written_word = write_word.toPlainText()
    is_correct = True
    if written_word == "":
        QMessageBox.critical(write_word, "BRAK SŁOWA", "Nie wpisano żadnego słowa.")
    else:
        for letter in written_word:
            if (ord(letter) < 65 or ord(letter) > 122 or (ord(letter) > 90 and ord(letter) < 97)) and (letter not in polish_letters):
                QMessageBox.critical(write_word, "NIEPRAWIDŁOWY ZNAK", f"We wprowadzonym słowie wykryto nieprawidłowy znak ({letter}). Wpisuj tylko litery.")
                is_correct = False
                break 
        if is_correct:
            written_word = written_word.upper()
            if written_word in all_words:
                QMessageBox.critical(write_word, "POWIELONE SŁOWO", "Wprowadzone słowo znajduje się już w bazie.")
            else:
                all_words.append(written_word)
                all_words.sort()
                with open("words_base.txt", "w", encoding="utf-8") as file:
                    for word in all_words:
                        file.write(word+'\n')
                load_words()
                if len(written_word) < 6:
                    easy_words.append(word)
                elif len(written_word) < 11:
                    medium_words.append(word)
                else:
                    hard_words.append(word)
                words_list_view.model().setStringList(all_words)
                scroll_widget.setMaximum(words_list_view.model().rowCount() - 1)
                message = QMessageBox(QMessageBox.Information,"SUKCES","Nowe słowo zostało pomyślnie wprowadzone do bazy.")
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
                write_word.clear()

def delete_word(write_word,words_list_view, scroll_widget):
    global all_words, easy_words, medium_words, hard_words
    written_word = write_word.toPlainText()
    written_word = written_word.upper()
    if written_word == "":
        QMessageBox.critical(write_word, "BRAK SŁOWA", "Nie wpisano żadnego słowa.")
    elif written_word in all_words:
        all_words.remove(written_word)
        with open("words_base.txt", 'w', encoding="utf-8") as file:
            for word in all_words:
                 file.write(word+'\n')
        if written_word in easy_words:
            easy_words.remove(word)
        elif written_word in medium_words:
            medium_words.remove(word)
        else:
            hard_words.remove(word)
        words_list_view.model().setStringList(all_words)
        scroll_widget.setMaximum(words_list_view.model().rowCount() - 1)
        message = QMessageBox(QMessageBox.Information,"SUKCES","Pomyślnie usunięto słowo z bazy.")
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
        write_word.clear()
    else:
        QMessageBox.critical(write_word, "BRAK SŁOWA", "Podanego słowa nie ma w bazie.")



