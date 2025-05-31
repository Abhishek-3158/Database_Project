#This module contains only the login window and it calls the login and sign in forms
#This is the module which is to be executed to run the SMS.
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_logInWindow(object):
    def __init__(self,window):
        self.window=window
        self.setupUi(window)
    def setupUi(self, Window):
        """setup is done here outside constructor"""
        Window.setObjectName("logInWindow")
        Window.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        #background section
        self.home_cover = QtWidgets.QLabel(self.centralwidget)
        self.home_cover.setGeometry(QtCore.QRect(0, 0, 641, 441))
        self.home_cover.setText("")
        self.home_cover.setPixmap(QtGui.QPixmap("icons/home_cover.jpg"))
        self.home_cover.setScaledContents(True)
        self.home_cover.setObjectName("home_cover")
        #LogIN button section
        self.log_in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_in_btn.setGeometry(QtCore.QRect(0, 430, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.log_in_btn.setFont(font)
        self.log_in_btn.setObjectName("log_in_btn")
        self.log_in_btn.clicked.connect(self.open_logInForm)
        #sign in button section
        self.sign_in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sign_in_btn.setGeometry(QtCore.QRect(320, 430, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sign_in_btn.setFont(font)
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.sign_in_btn.clicked.connect(self.open_signInForm)

        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
    def retranslateUi(self, logInWindow):
        _translate = QtCore.QCoreApplication.translate
        logInWindow.setWindowTitle(_translate("logInWindow", "Student Record Management System"))
        self.log_in_btn.setText(_translate("logInWindow", "Log In"))
        self.sign_in_btn.setText(_translate("logInWindow", "Sign In"))
    def open_logInForm(self):
        """logIn button function to open the login form"""
        from logInForm import LoginForm
        self.form = LoginForm(self)
        self.form.show()
    def open_signInForm(self):
        """sign in button functin to open signin form"""
        from logInForm import SigninForm
        self.form=SigninForm(self)
        self.form.show()
    def open_sms(self):
        """opens the main window of the SMS."""
        from mainWindow import Ui_MainWindow
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)

def main():
    import sys
    """this section launches the application,"""
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_logInWindow(Window)
    Window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()