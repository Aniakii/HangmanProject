from PyQt5 import QtCore, QtGui, QtWidgets
from gui_functionality import start_game, get_guessed_letter

class Ui_GameWindow(object):
    def setupUi(self, Game_Window):
        Game_Window.setObjectName("Game_Window")
        Game_Window.resize(539, 448)
        self.centralwidget = QtWidgets.QWidget(Game_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.word_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.word_browser.setGeometry(QtCore.QRect(20, 20, 491, 51))
        self.word_browser.setObjectName("word_browser")
        self.write_letter_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.write_letter_textEdit.setGeometry(QtCore.QRect(20, 320, 121, 41))
        self.write_letter_textEdit.setObjectName("write_letter_textEdit")
        self.guess_button = QtWidgets.QPushButton(self.centralwidget)
        self.guess_button.setGeometry(QtCore.QRect(20, 370, 121, 23))
        self.guess_button.setObjectName("guess_button")
        self.reset_game_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_game_button.setGeometry(QtCore.QRect(300, 380, 75, 23))
        self.reset_game_button.setObjectName("reset_game_button")
        self.to_menu_button = QtWidgets.QPushButton(self.centralwidget)
        self.to_menu_button.setGeometry(QtCore.QRect(380, 380, 75, 23))
        self.to_menu_button.setObjectName("to_menu_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(460, 380, 75, 23))
        self.exit_button.setObjectName("exit_button")
        self.hangman_view = QtWidgets.QLabel(self.centralwidget)
        self.hangman_view.setGeometry(QtCore.QRect(30, 80, 281, 221))
        self.hangman_view.setText("")
        self.hangman_view.setPixmap(QtGui.QPixmap("hangman_pictures/hangman0.png"))
        self.hangman_view.setObjectName("hangman_view")
        self.mistakes_label = QtWidgets.QLabel(self.centralwidget)
        self.mistakes_label.setGeometry(QtCore.QRect(350, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(18)
        self.mistakes_label.setFont(font)
        self.mistakes_label.setObjectName("mistakes_label")
        self.mistakes_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.mistakes_browser.setGeometry(QtCore.QRect(370, 140, 71, 51))
        self.mistakes_browser.setObjectName("textBrowser")
        Game_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Game_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        Game_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Game_Window)
        self.statusbar.setObjectName("statusbar")
        Game_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Game_Window)
        QtCore.QMetaObject.connectSlotsByName(Game_Window)

    def retranslateUi(self, Game_Window):
        _translate = QtCore.QCoreApplication.translate
        Game_Window.setWindowTitle(_translate("Game_Window", "Hangman Game"))
        # self.word_browser.setHtml('<html><body><div style="display: flex; height: 100%; align-items: center; justify-content: center;">Your text goes here</div></body></html>')
        self.word_browser.setHtml(_translate("Game_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:100.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.write_letter_textEdit.setHtml(_translate("Game_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.guess_button.setText(_translate("Game_Window", "Guess a letter or word"))
        self.reset_game_button.setText(_translate("Game_Window", "Reset Game"))
        self.to_menu_button.setText(_translate("Game_Window", "Back to menu"))
        self.exit_button.setText(_translate("Game_Window", "Exit"))
        self.mistakes_label.setText(_translate("Game_Window", "Mistakes left:"))
        self.word_browser.setStyleSheet('''
        QTextBrowser {
            font-size: 24px;
            text-align: center;
            line-height: 1.5;
            vertical-align: middle;
        }
''')
        self.mistakes_browser.setStyleSheet( '''
        QTextBrowser {
        font-size: 30px;
        text-align: center;
        line-height: 1.5;
        vertical-align: middle;
        }
        ''')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Game_Window = QtWidgets.QMainWindow()
    ui = Ui_GameWindow()
    ui.setupUi(Game_Window)
    start_game(ui.word_browser,ui.mistakes_browser)
    ui.guess_button.clicked.connect(lambda: get_guessed_letter(ui.write_letter_textEdit,ui.hangman_view,ui.mistakes_browser,ui.word_browser))
    Game_Window.show()
    sys.exit(app.exec_())
