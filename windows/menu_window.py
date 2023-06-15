from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(510, 396)
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_game_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_game_button.setGeometry(QtCore.QRect(190, 90, 151, 41))
        self.start_game_button.setObjectName("start_game_button")
        self.add_word_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_word_button.setGeometry(QtCore.QRect(190, 140, 151, 41))
        self.add_word_button.setObjectName("add_word_button")
        self.show_words_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_words_button.setGeometry(QtCore.QRect(190, 240, 151, 41))
        self.show_words_button.setObjectName("show_words_button")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(110, 30, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(36)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(190, 290, 151, 41))
        self.exit_button.setObjectName("exit_button")
        self.delete_word_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_word_button.setGeometry(QtCore.QRect(190, 190, 151, 41))
        self.delete_word_button.setObjectName("delete_word_button")
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        MenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "Hangman Game Menu"))
        self.start_game_button.setText(_translate("MenuWindow", "Start a new game"))
        self.add_word_button.setText(_translate("MenuWindow", "Add new word"))
        self.show_words_button.setText(_translate("MenuWindow", "Show all words"))
        self.title_label.setText(_translate("MenuWindow", "H A N G M A N"))
        self.exit_button.setText(_translate("MenuWindow", "Exit"))
        self.delete_word_button.setText(_translate("MenuWindow", "Delete word"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)
    MenuWindow.show()
    sys.exit(app.exec_())
