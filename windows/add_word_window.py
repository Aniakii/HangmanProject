from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddWordWindow(object):
    def setupUi(self, AddWordWindow):
        AddWordWindow.setObjectName("AddWordWindow")
        AddWordWindow.resize(356, 264)
        self.centralwidget = QtWidgets.QWidget(AddWordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enter_word_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_word_label.setGeometry(QtCore.QRect(50, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(24)
        self.enter_word_label.setFont(font)
        self.enter_word_label.setObjectName("enter_word_label")
        self.enter_word_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.enter_word_textEdit.setGeometry(QtCore.QRect(50, 80, 241, 71))
        self.enter_word_textEdit.setObjectName("enter_word_textEdit")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(50, 180, 111, 31))
        self.add_button.setObjectName("add_button")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(180, 180, 111, 31))
        self.return_button.setObjectName("return_button")
        AddWordWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddWordWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 21))
        self.menubar.setObjectName("menubar")
        AddWordWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddWordWindow)
        self.statusbar.setObjectName("statusbar")
        AddWordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddWordWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWordWindow)

    def retranslateUi(self, AddWordWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWordWindow.setWindowTitle(_translate("AddWordWindow", "Hangman Add Word"))
        self.enter_word_label.setText(_translate("AddWordWindow", "Enter a word to add:"))
        self.enter_word_textEdit.setHtml(_translate("AddWordWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.add_button.setText(_translate("AddWordWindow", "Add word"))
        self.return_button.setText(_translate("AddWordWindow", "Return to menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddWordWindow = QtWidgets.QMainWindow()
    ui = Ui_AddWordWindow()
    ui.setupUi(AddWordWindow)
    AddWordWindow.show()
    sys.exit(app.exec_())
