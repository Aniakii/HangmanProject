from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListWindow(object):
    def setupUi(self, ListWindow):
        ListWindow.setObjectName("ListWindow")
        ListWindow.setFixedSize(364, 493)
        self.centralwidget = QtWidgets.QWidget(ListWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.words_list_view = QtWidgets.QListView(self.centralwidget)
        self.words_list_view.setGeometry(QtCore.QRect(10, 90, 341, 301))
        self.words_list_view.setObjectName("words_list_view")
        self.words_verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.words_verticalScrollBar.setGeometry(QtCore.QRect(330, 90, 21, 301))
        self.words_verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.words_verticalScrollBar.setObjectName("words_verticalScrollBar")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(120, 400, 111, 41))
        self.return_button.setObjectName("back_to_menu_button")
        self.list_label = QtWidgets.QLabel(self.centralwidget)
        self.list_label.setGeometry(QtCore.QRect(80, 40, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(24)
        self.list_label.setFont(font)
        self.list_label.setObjectName("list_label")
        ListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 21))
        self.menubar.setObjectName("menubar")
        ListWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListWindow)
        self.statusbar.setObjectName("statusbar")
        ListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ListWindow)
        QtCore.QMetaObject.connectSlotsByName(ListWindow)

    def retranslateUi(self, ListWindow):
        _translate = QtCore.QCoreApplication.translate
        ListWindow.setWindowTitle(_translate("ListWindow", "Hangman Words List"))
        self.return_button.setText(_translate("ListWindow", "Return to menu"))
        self.list_label.setText(_translate("ListWindow", "List of all words:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListWindow = QtWidgets.QMainWindow()
    ui = Ui_ListWindow()
    ui.setupUi(ListWindow)
    ListWindow.show()
    sys.exit(app.exec_())
