#This module contains and performs all the task related to the database.
from sqlite3 import *
from PyQt5.QtWidgets import QMessageBox
class SMSDB():
    def __init__(self):
        """database creation in constructor"""
        self.conn=connect('SMSDatabase.db')#connecting database
        self.cur=self.conn.cursor()#cursor for database
        #creating Admin table stores tha admin login details)
        self.cur.execute("""create table if not exists
                            Admin(
                            username primary key not null,
                            password,name,contact);
                            """)
        #creating student table stores the personal details
        self.cur.execute("""create table if not exists
                            Student(
                            reg_no primary key not null,
                            roll,name,course,contact,address);
                            """)
        #creating fees table stores the fee detail of studnet
        self.cur.execute("""create table if not exists
                            Fees(
                            reg_no primary key not null,
                            sem1,sem2,sem3,sem4,sem5,sem6);
                            """)
        #creating attendance table stores attendace of student
        self.cur.execute("""create table if not exists
                            Attendance(
                            reg_no primary key not null,
                            sem1,sem2,sem3,sem4,sem5,sem6);
                            """)
        #creating remark table for remark statement
        self.cur.execute("""create table if not exists
                            Remark(reg_no primary key not null,stmt);""")
    def conn_close(self):
        """closes database connection"""
        self.conn.commit()#ensuring all the transactions are saved before closing.
        self.conn.close()
    def insert_admin(self,un,pwd,fn,mob):
        """adding new admin through sign in process"""
        flag=False
        if not self.check_exist(un):
            self.cur.execute('insert into Admin(username,password,name,contact)values(?,?,?,?)',(un,pwd,fn,mob))
            self.conn.commit()
            flag=True
        return flag
    def insertStud(self,reg,nm,roll,no,sub,add,fee,atnd,rmrk):
        flag=False
        if not self.stud_exist(reg):
            self.cur.execute('insert into Student values(?,?,?,?,?,?)',(reg,roll,nm,sub,no,add))
            self.cur.execute('insert into Fees values(?,?,?,?,?,?,?)',(reg,fee[0],fee[1],fee[2],fee[3],fee[4],fee[5]))
            self.cur.execute('insert into Attendance values(?,?,?,?,?,?,?)',(reg,atnd[0],atnd[1],atnd[2],atnd[3],atnd[4],atnd[5]))
            self.cur.execute('insert into Remark values(?,?)',(reg,rmrk))
            self.conn.commit()
            flag=True
        return flag
    def update_admin(self,un,pswd,nm,no):
        self.cur.execute("update Admin set name=?,contact=?,password=? where username=?",(nm,no,pswd,un))
    def updateStud(self,reg,nm,roll,no,sub,add,fee,atnd,rmrk):
        self.cur.execute("""update Student 
                            set roll=?,name=?,course=?,contact=?,address=?
                            where reg_no=?""",(roll,nm,sub,no,add,reg))
        self.cur.execute("""update Fees
                            set sem1=?,sem2=?,sem3=?,sem4=?,sem5=?,sem6=?
                            where reg_no=?""",(fee[0],fee[1],fee[2],fee[3],fee[4],fee[5],reg))
        self.cur.execute("""update Attendance
                            set sem1=?,sem2=?,sem3=?,sem4=?,sem5=?,sem6=?
                            where reg_no=?""",(atnd[0],atnd[1],atnd[2],atnd[3],atnd[4],atnd[5],reg))
        self.cur.execute("""update Remark set stmt=? where reg_no=?""",(rmrk,reg))
    def delete_admin(self,un):
        """delete admin from database"""
        self.conn.execute('delete from Admin where username=?',(un,))
        self.conn.commit()
    def deleteStud(self,table,regNo):
        if table=="Student":self.cur.execute('delete from Student where reg_no=?',(regNo,))
        if table=="Fees":self.cur.execute('delete from Fees where reg_no=?', (regNo,))
        if table=="Attendance":self.cur.execute('delete from Attendance where reg_no=?',(regNo,))
        if table=="Remark":self.cur.execute('delete from Remark where reg_no=?',(regNo,))
    def verify_admin(self,un,pswd):
        """verifies admin for login"""
        """matches password of admin"""
        flag=False
        if self.check_exist(un):
            self.cur.execute('select password from Admin where username=?',(un,))
            if pswd == self.cur.fetchone()[0]:flag=True
        return flag

    def check_exist(self,id):
        """checks if the id already exists or not"""
        flag=True
        self.cur.execute('select rowid from Admin where username = ?', (id,))
        if self.cur.fetchone() is None:flag=False
        return flag
    def stud_exist(self,id):
        flag=True
        self.cur.execute('select rowid from Student where reg_no=?',(id,))
        if self.cur.fetchone() is None:flag=False
        return flag
    def fetchAdmin(self,uid):
         return self.cur.execute('select * from Admin where username=?',(uid,)).fetchone()
    def fetchStud(self,table,regNo):
        if table=="Student":
            return self.cur.execute('select * from Student where reg_no =?',(regNo,)).fetchone()
        if table=="Fees":
            return self.cur.execute('select * from Fees where reg_no =?', (regNo,)).fetchone()
        if table=="Attendance":
            return self.cur.execute('select * from Attendance where reg_no =?', (regNo,)).fetchone()
        if table=="Remark":
            return self.cur.execute('select * from Remark where reg_no =?', (regNo,)).fetchone()
    def query(self,sql):
        return  self.cur.execute(sql)
def show_msg(str):
    """to show any messaage through dialog box."""
    msg = QMessageBox()
    msg.setWindowTitle(' ')
    msg.setText(str)
    msg.exec_()
def confirm_msg(str):
    flag=False
    msg=QMessageBox()
    msg.setWindowTitle(' ')
    msg.setText(str)
    msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
    reply=msg.exec_()
    if reply==QMessageBox.Yes:flag=True
    return flag
"""For Trial Run""
d=SMSDB()
print(d.fetchStud('Attendance','206202101048'))
"""