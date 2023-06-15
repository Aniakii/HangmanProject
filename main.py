import sys
from PyQt5 import QtWidgets
from windows.menu_window import Ui_MenuWindow
from windows.game_window import Ui_GameWindow
from windows.add_word_window import Ui_AddWordWindow
from windows.delete_word_window import Ui_DeleteWordWindow
from windows.words_list_window import Ui_ListWindow
from windows.choose_level_window import Ui_ChooseLevelWindow
from gui_functionality import start_game, get_guessed_letter, open_different_window, setup_list_view, add_word, get_all_words, delete_word


def execute_program():
    app = QtWidgets.QApplication(sys.argv)
    get_all_words()

    Menu_Window = QtWidgets.QMainWindow()
    ui_menu = Ui_MenuWindow()
    ui_menu.setupUi(Menu_Window)

    Choose_Level_Window = QtWidgets.QMainWindow()
    ui_choose_level = Ui_ChooseLevelWindow()
    ui_choose_level.setupUi(Choose_Level_Window)

    Game_Window = QtWidgets.QMainWindow()
    ui_game = Ui_GameWindow()
    ui_game.setupUi(Game_Window)

    Add_Word_Window = QtWidgets.QMainWindow()
    ui_add_word = Ui_AddWordWindow()
    ui_add_word.setupUi(Add_Word_Window)

    Delete_Word_Window = QtWidgets.QMainWindow()
    ui_delete_word = Ui_DeleteWordWindow()
    ui_delete_word.setupUi(Delete_Word_Window)

    Words_List_Window = QtWidgets.QMainWindow()
    ui_words_list = Ui_ListWindow()
    ui_words_list.setupUi(Words_List_Window)
    setup_list_view(ui_words_list,ui_words_list.words_list_view,ui_words_list.words_verticalScrollBar)

    # ui_menu.start_game_button.clicked.connect(lambda: start_game(ui_game.word_browser,ui_game.mistakes_browser,ui_game.hangman_view,Menu_Window, Game_Window))
    ui_menu.start_game_button.clicked.connect(lambda: open_different_window(Menu_Window, Choose_Level_Window))
    ui_menu.add_word_button.clicked.connect(lambda: open_different_window(Menu_Window,Add_Word_Window))
    ui_menu.delete_word_button.clicked.connect(lambda: open_different_window(Menu_Window, Delete_Word_Window))
    ui_menu.show_words_button.clicked.connect(lambda: open_different_window(Menu_Window, Words_List_Window))
    ui_menu.exit_button.clicked.connect(lambda: QtWidgets.QApplication.quit())

    ui_choose_level.easy_button.clicked.connect(lambda: start_game(ui_game.word_browser,ui_game.mistakes_browser,ui_game.hangman_view, Choose_Level_Window, Game_Window, 1))
    ui_choose_level.medium_button.clicked.connect(lambda: start_game(ui_game.word_browser,ui_game.mistakes_browser,ui_game.hangman_view, Choose_Level_Window, Game_Window, 2))
    ui_choose_level.hard_button.clicked.connect(lambda: start_game(ui_game.word_browser,ui_game.mistakes_browser,ui_game.hangman_view, Choose_Level_Window, Game_Window, 3))
    ui_choose_level.random_button.clicked.connect(lambda: start_game(ui_game.word_browser,ui_game.mistakes_browser,ui_game.hangman_view, Choose_Level_Window, Game_Window, 0))
    ui_choose_level.return_to_menu_button.clicked.connect(lambda: open_different_window(Choose_Level_Window, Menu_Window))

    ui_add_word.return_button.clicked.connect(lambda: open_different_window(Add_Word_Window,Menu_Window))
    ui_add_word.add_button.clicked.connect(lambda : add_word(ui_add_word.enter_word_textEdit,ui_words_list,ui_words_list.words_list_view,ui_words_list.words_verticalScrollBar))
    
    ui_delete_word.return_button.clicked.connect(lambda: open_different_window(Delete_Word_Window,Menu_Window))
    ui_delete_word.delete_button.clicked.connect(lambda: delete_word(ui_delete_word.enter_word_textEdit,ui_words_list,ui_words_list.words_list_view,ui_words_list.words_verticalScrollBar))

    ui_words_list.return_button.clicked.connect(lambda: open_different_window(Words_List_Window,Menu_Window))
    
    ui_game.guess_button.clicked.connect(lambda: get_guessed_letter(ui_game.write_letter_textEdit,ui_game.hangman_view,ui_game.mistakes_browser,ui_game.word_browser, Menu_Window, Game_Window))
    ui_game.reset_game_button.clicked.connect(lambda: start_game(ui_game.word_browser,ui_game.mistakes_browser,ui_game.hangman_view,Menu_Window, Game_Window))
    ui_game.to_menu_button.clicked.connect(lambda: open_different_window(Game_Window,Menu_Window))
    ui_game.exit_button.clicked.connect(lambda: QtWidgets.QApplication.quit())
    Menu_Window.show()
    sys.exit(app.exec_())


execute_program()