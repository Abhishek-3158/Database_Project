#This module contains main Window of the SMS.
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """setting up the window"""
        self.window=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.showMaximized()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#adminBtn{""font: 75 14pt \"Palatino Linotype\";}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#sideMenu{background:rgb(0, 170, 127);}\n"
                                        "#mainBody{background:rgb(255, 255, 255);}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #side menu section
        self.sideMenu = QtWidgets.QWidget(self.centralwidget)
        self.sideMenu.setMaximumSize(QtCore.QSize(360, 16777215))
        self.sideMenu.setObjectName("sideMenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sideMenu)
        self.verticalLayout.setObjectName("verticalLayout")
        #symbol section
        self.symbolFrame = QtWidgets.QFrame(self.sideMenu)
        self.symbolFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.symbolFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.symbolFrame.setObjectName("symbolFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.symbolFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.symbol = QtWidgets.QLabel(self.symbolFrame)
        self.symbol.setMaximumSize(QtCore.QSize(150, 150))
        self.symbol.setFrameShape(QtWidgets.QFrame.Box)
        self.symbol.setFrameShadow(QtWidgets.QFrame.Raised)
        self.symbol.setLineWidth(5)
        self.symbol.setText("")
        self.symbol.setPixmap(QtGui.QPixmap("icons/logo.png"))
        self.symbol.setScaledContents(True)
        self.symbol.setAlignment(QtCore.Qt.AlignCenter)
        self.symbol.setObjectName("symbol")
        self.verticalLayout_3.addWidget(self.symbol, 0, QtCore.Qt.AlignHCenter)
        #sms label section
        self.sms_txt = QtWidgets.QLabel(self.symbolFrame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sms_txt.setFont(font)
        self.sms_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.sms_txt.setObjectName("sms_txt")
        self.sms_txt.setWordWrap(True)
        self.verticalLayout_3.addWidget(self.sms_txt, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.symbolFrame)
        #button section
        self.btnFrame = QtWidgets.QFrame(self.sideMenu)
        self.btnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnFrame.setObjectName("btnFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.btnFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        #administration button
        self.adminBtn = QtWidgets.QPushButton(self.btnFrame)
        self.adminBtn.setObjectName("adminBtn")
        self.adminBtn.clicked.connect(self.openAdmin)
        self.verticalLayout_2.addWidget(self.adminBtn)
        #student button
        self.studBtn = QtWidgets.QPushButton(self.btnFrame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setWeight(50)
        self.studBtn.setFont(font)
        self.studBtn.setObjectName("studBtn")
        self.studBtn.clicked.connect(self.openStud)
        self.verticalLayout_2.addWidget(self.studBtn)
        #record button
        self.recBtn = QtWidgets.QPushButton(self.btnFrame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.recBtn.setFont(font)
        self.recBtn.setObjectName("recBtn")
        self.recBtn.clicked.connect(self.openRecord)
        self.verticalLayout_2.addWidget(self.recBtn)
        self.verticalLayout.addWidget(self.btnFrame)
        #logout section
        self.logFrame = QtWidgets.QFrame(self.sideMenu)
        self.logFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logFrame.setObjectName("logFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.logFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #log out button
        self.logoutBtn = QtWidgets.QPushButton(self.logFrame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.logoutBtn.setFont(font)
        self.logoutBtn.setObjectName("logoutBtn")
        self.logoutBtn.clicked.connect(self.prfmLogOut)
        self.logoutBtn.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.logoutBtn, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.logFrame)
        self.horizontalLayout.addWidget(self.sideMenu)
        #main body section
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setObjectName("mainBody")
        self.layout=QtWidgets.QHBoxLayout(self.mainBody)
        self.horizontalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Record Management System"))
        self.sms_txt.setText(_translate("MainWindow", "Student Record Management System"))
        self.adminBtn.setText(_translate("MainWindow", "Administration"))
        self.studBtn.setText(_translate("MainWindow", "Student"))
        self.recBtn.setText(_translate("MainWindow", "Records"))
        self.logoutBtn.setText(_translate("MainWindow", "Log Out"))

    def openStud(self):
        from studFrame import Ui_studFrame
        self.studFrame=QtWidgets.QFrame()
        self.stud=Ui_studFrame()
        self.stud.setupUi(self.studFrame)
        self.show(self.studFrame)
    def show(self,w):
        if self.layout.isEmpty():self.layout.addWidget(w)
        else:self.layout.replaceWidget(self.layout.itemAt(0).widget(),w)
    def openAdmin(self):
        from adminFrame import Ui_adminFrame
        self.adminFrame=QtWidgets.QFrame()
        self.admin=Ui_adminFrame()
        self.admin.setupUi(self.adminFrame)
        self.show(self.adminFrame)
    def openRecord(self):
        from recordFrame import Ui_recordFrame
        self.recordFrame=QtWidgets.QFrame()
        self.record=Ui_recordFrame()
        self.record.setupUi(self.recordFrame)
        self.show(self.recordFrame)
    def prfmLogOut(self):
        from SMS import Ui_logInWindow
        self.window.showNormal()
        ui=Ui_logInWindow(self.window)

def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

"""For Trial Run""
if __name__ == "__main__":run()
"""