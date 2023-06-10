from PyQt5 import QtCore, QtGui, QtWidgets
from gui_functionality import start_game

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_game_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_game_button.setGeometry(QtCore.QRect(190, 90, 151, 41))
        self.start_game_button.setObjectName("start_game_button")
        self.add_word_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_word_button.setGeometry(QtCore.QRect(190, 140, 151, 41))
        self.add_word_button.setObjectName("add_word_button")
        self.show_words_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_words_button.setGeometry(QtCore.QRect(190, 190, 151, 41))
        self.show_words_button.setObjectName("show_words_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(190, 240, 151, 41))
        self.exit_button.setObjectName("exit_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.game_window = None
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hangman Game Menu"))
        self.start_game_button.setText(_translate("MainWindow", "Start a new game"))
        self.add_word_button.setText(_translate("MainWindow", "Add new word"))
        self.show_words_button.setText(_translate("MainWindow", "Show all words"))
        self.label.setText(_translate("MainWindow", "H A N G M A N"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.start_game_button.clicked.connect(lambda: start_game(MainWindow))

    MainWindow.show()
    sys.exit(app.exec_())
