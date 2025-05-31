#This module objective is to view the admin / student record in tabular form.
from PyQt5 import QtCore, QtGui, QtWidgets
from Database import *
class Ui_recordFrame(object):
    def setupUi(self, recordFrame):
        recordFrame.setObjectName("recordFrame")
        recordFrame.resize(700, 700)
        recordFrame.setMinimumSize(QtCore.QSize(700, 700))
        recordFrame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(recordFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        #button section
        self.btnFrame = QtWidgets.QFrame(recordFrame)
        self.btnFrame.setMinimumSize(QtCore.QSize(0, 75))
        self.btnFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btnFrame.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.btnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btnFrame.setObjectName("btnFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.btnFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #admin button
        self.adminBtn = QtWidgets.QPushButton(self.btnFrame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.adminBtn.setFont(font)
        self.adminBtn.setStyleSheet("background:rgb(255, 255, 255);\n"
                                        "border-radius:15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adminBtn.setIcon(icon)
        self.adminBtn.setIconSize(QtCore.QSize(40, 40))
        self.adminBtn.setObjectName("adminBtn")
        self.adminBtn.clicked.connect(self.openAdmin)
        self.horizontalLayout.addWidget(self.adminBtn)
        #stud button
        self.studBtn = QtWidgets.QPushButton(self.btnFrame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.studBtn.setFont(font)
        self.studBtn.setStyleSheet("background:rgb(255, 255, 255);\n"
                                        "border-radius:15px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.studBtn.setIcon(icon1)
        self.studBtn.setIconSize(QtCore.QSize(40, 40))
        self.studBtn.setObjectName("studBtn")
        self.studBtn.clicked.connect(self.openStud)
        self.horizontalLayout.addWidget(self.studBtn)
        self.verticalLayout.addWidget(self.btnFrame)
        #table section
        self.tableFrame = QtWidgets.QFrame(recordFrame)
        self.tableFrame.setMinimumSize(QtCore.QSize(0, 600))
        self.tableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableFrame.setObjectName("tableFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.tableFrame)
        self.gridLayout.setObjectName("gridLayout")
        #table
        self.recordTable = QtWidgets.QTableWidget(self.tableFrame)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.recordTable.setFont(font)
        self.recordTable.setObjectName("recordTable")
        self.gridLayout.addWidget(self.recordTable, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tableFrame)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-top-right-radius:15px;\n"
                                    "border-top-left-radius:15px;\n"
                                    "background:rgb(0, 170, 127)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.tableFrame)

        self.retranslateUi(recordFrame)
        QtCore.QMetaObject.connectSlotsByName(recordFrame)

    def retranslateUi(self, recordFrame):
        _translate = QtCore.QCoreApplication.translate
        recordFrame.setWindowTitle(_translate("recordFrame", "recordFrame"))
        self.adminBtn.setText(_translate("recordFrame", "Admin Record"))
        self.studBtn.setText(_translate("recordFrame", "Student Record"))
        self.label.setText(_translate("recordFrame", "Record"))

    def openAdmin(self):
        fields=['User Name','Password','Full Name','Contact']
        self.fillTable('Admin',4,fields)
    def openStud(self):
        fields=['Registration No','Roll No','Name','Course','Contact','Address']
        self.fillTable('Student',6,fields)
    def fillTable(self,table,no,fields):
        db = SMSDB()
        rowNo=db.query('select count(*) from '+table).fetchone()[0]
        self.recordTable.setRowCount(rowNo)
        self.recordTable.setColumnCount(no)
        self.recordTable.setHorizontalHeaderLabels(fields)
        records = db.query('select * from '+table)
        for row,record in enumerate(records):
            for colomn,item in enumerate(record):
                self.recordTable.setItem(row,colomn,QtWidgets.QTableWidgetItem(str(item)))
        db.conn_close()


"""This is for trial run""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    recordFrame = QtWidgets.QFrame()
    ui = Ui_recordFrame()
    ui.setupUi(recordFrame)
    recordFrame.show()
    sys.exit(app.exec_())
"""