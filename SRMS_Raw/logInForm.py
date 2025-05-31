#This module contains LogIn Form and SignIn Form with their functions
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
from Database import *

class LoginForm(QWidget):
	def __init__(self,parent):
		"""setup is done here"""
		super().__init__()
		self.parent = parent
		self.setWindowTitle('LogIn Form')
		self.resize(500, 120)
		#layout section
		layout = QGridLayout()
		self.setLayout(layout)
		#username section
		label_name = QLabel('<font size="5"> Username </font>')
		self.lineEdit_username = QLineEdit()
		font = QtGui.QFont()
		font.setPointSize(10)
		self.lineEdit_username.setFont(font)
		self.lineEdit_username.setPlaceholderText('Please enter your username')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)
		#password section
		label_password = QLabel('<font size="5"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setFont(font)
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)
		#submit button section
		font.setBold(True)
		button_login = QPushButton('Login')
		button_login.setFont(font)
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)
		
	def check_password(self):
		"""logIn Form submit function"""
		if not self.lineEdit_username.text().isalnum(): show_msg('Enter valid user name.')
		else:
			db=SMSDB()#connecting database
			if db.verify_admin(self.lineEdit_username.text(),self.lineEdit_password.text()):
				self.close()
				self.parent.open_sms()
			else:
				show_msg('Incorrect Credentials')
			db.conn_close()#disconnecting database


class SigninForm(QWidget):
	def __init__(self,parent):
		self.parent=parent
		"""setup is done"""
		super().__init__()
		self.setWindowTitle('SignIn Form')
		self.resize(600,400)
		#layout section
		layout = QGridLayout()
		self.setLayout(layout)
		#name section
		label_f_name=QLabel('<font size="5">Name </font>')
		self.lineEdit_f_name = QLineEdit()
		font = QtGui.QFont()
		font.setPointSize(10)
		self.lineEdit_f_name.setFont(font)
		self.lineEdit_f_name.setPlaceholderText('Please enter full name')
		layout.addWidget(label_f_name,0,0)
		layout.addWidget(self.lineEdit_f_name,0,1)
		#username section
		label_u_name = QLabel('<font size="5"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setFont(font)
		self.lineEdit_username.setPlaceholderText('Please enter username')
		layout.addWidget(label_u_name,1,0)
		layout.addWidget(self.lineEdit_username,1,1)
		#contact section
		label_mobile=QLabel('<font size="5">Mobile No </font>')
		self.lineEdit_mob=QLineEdit()
		self.lineEdit_mob.setFont(font)
		self.lineEdit_mob.setPlaceholderText('Please enter mobile no')
		layout.addWidget(label_mobile,2,0)
		layout.addWidget(self.lineEdit_mob,2,1)
		#password section
		label_password = QLabel('<font size="5"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setFont(font)
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)
		layout.addWidget(label_password,3,0)
		layout.addWidget(self.lineEdit_password,3,1)
		#confirm password section
		confirm=QLabel('<font size="5">Confirm Password </font>')
		self.lineEdit_confirm = QLineEdit()
		self.lineEdit_confirm.setFont(font)
		self.lineEdit_confirm.setPlaceholderText('Please confirm password')
		self.lineEdit_confirm.setEchoMode(QLineEdit.EchoMode.Password)
		layout.addWidget(confirm, 4, 0)
		layout.addWidget(self.lineEdit_confirm, 4, 1)
		#submit button section
		font.setBold(True)
		button_signin = QPushButton('Sign in')
		button_signin.setFont(font)
		button_signin.clicked.connect(self.register_admin)
		layout.addWidget(button_signin, 5, 0, 1, 2)

	def register_admin(self):
		"""Sign In Form submit button function"""
		#fetching all data from form
		un=self.lineEdit_username.text()
		fn=self.lineEdit_f_name.text()
		pswd=self.lineEdit_password.text()
		no=self.lineEdit_mob.text()
		cnfrm=self.lineEdit_confirm.text()
		#applying validations
		for name in fn.split():
			if not name.isalpha():
				show_msg('Enter valid name.')
				break
		if not un.isalnum():show_msg('Enter valid user name.')
		elif not no.isdigit():show_msg('Enter valid Mobile No.')
		elif len(no)!=10:show_msg('Enter valid length Mobile No.')
		elif pswd != cnfrm:show_msg('Both password does not match.')
		else:
			db=SMSDB()#connnecting DB
			if db.insert_admin(un,pswd,fn,no):
				show_msg('Admin Registered.')
				self.close()
			else:show_msg('Username already taken.')
			db.conn_close()#disconnecting DB
