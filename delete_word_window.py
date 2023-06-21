from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteWordWindow(object):
    def setupUi(self, DeleteWordWindow):
        DeleteWordWindow.setObjectName("DeleteWordWindow")
        DeleteWordWindow.setFixedSize(478, 262)
        DeleteWordWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(DeleteWordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enter_word_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_word_label.setGeometry(QtCore.QRect(100, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(24)
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(110, 180, 111, 31))
        self.delete_button.setObjectName("delete_button")
        self.delete_button.setDefault(True)
        self.enter_word_label.setFont(font)
        self.enter_word_label.setObjectName("enter_word_label")
        self.enter_word_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.enter_word_textEdit.setGeometry(QtCore.QRect(110, 80, 251, 71))
        self.enter_word_textEdit.setObjectName("enter_word_textEdit")
        self.return_button = QtWidgets.QPushButton(self.centralwidget)
        self.return_button.setGeometry(QtCore.QRect(250, 180, 111, 31))
        self.return_button.setObjectName("return_button")
        DeleteWordWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DeleteWordWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 21))
        self.menubar.setObjectName("menubar")
        DeleteWordWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DeleteWordWindow)
        self.statusbar.setObjectName("statusbar")
        DeleteWordWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DeleteWordWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteWordWindow)

    def retranslateUi(self, DeleteWordWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteWordWindow.setWindowTitle(_translate("DeleteWordWindow", "Hangman Delete Word"))
        self.enter_word_label.setText(_translate("DeleteWordWindow", "Enter a word to delete:"))
        self.enter_word_textEdit.setHtml(_translate("DeleteWordWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.delete_button.setText(_translate("DeleteWordWindow", "Delete word"))
        self.return_button.setText(_translate("DeleteWordWindow", "Return to menu"))

