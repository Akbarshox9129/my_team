import sqlite3
from PyQt5.QtWidgets import QApplication,QWidget,QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import QLabel,QRadioButton,QPushButton,QLineEdit
from PyQt5.QtGui import QFont
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.con=sqlite3.connect("MEVA.db")
        self.k=self.con.cursor()
        self.setWindowTitle("DATABASE AND PyQt5")
        self.setGeometry(200,200,1200,800)
        self.start()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",30))
        ob.move(x,y)
    def start(self):
        self.create()
        self.l1=QLabel("ID",self)
        self.font(self.l1,50,50)
        self.l2=QLabel("NAME",self)
        self.font(self.l2,50,120)
        self.l3=QLabel("PRICE",self)
        self.font(self.l3,50,190)
        self.k1=QLineEdit(self)
        self.font(self.k1,250,50)
        self.k1.setPlaceholderText("idni kiriting....")
        self.k2=QLineEdit(self)
        self.font(self.k2,250,120)
        self.k2.setPlaceholderText("nomini kiriting....")
        self.k3=QLineEdit(self)
        self.font(self.k3,250,190)
        self.k3.setPlaceholderText("narxini kiriting....")
        self.add=QPushButton("ADD",self)
        self.font(self.add,50,260)
        self.delete=QPushButton("DELETE",self)
        self.font(self.delete,170,260)
        self.update=QPushButton("UPDATE",self)
        self.font(self.update,355,260)
        self.v1=QRadioButton("Id",self)
        self.font(self.v1,750,50)
        self.v2=QRadioButton("Name",self)
        self.font(self.v2,750,120)
        self.v3=QRadioButton("Price",self)
        self.font(self.v3,750,190)
        self.s=QLineEdit(self)
        self.font(self.s,750,260)
        self.s.setPlaceholderText("Searching....")
        self.search=QPushButton("SEARCH",self)
        self.font(self.search,750,330)
        self.printf=QTableWidget(3,3,self)
        self.printf.setFont(QFont("Times",20))
        self.printf.setGeometry(50,400,350,150)
        self.printf.setHorizontalHeaderLabels(['id',"name","price"])

        self.add.clicked.connect(self.ADD)
        self.delete.clicked.connect(self.DELETE)
        self.update.clicked.connect(self.UPDATE)
        self.search.clicked.connect(self.SEARCH)
    def ADD(self):
        if self.k1.text()!="" and self.k2.text()!="" and self.k3.text()!="":
            a=int(self.k1.text())
            b=self.k2.text()
            c=float(self.k3.text())
            self.insert(a,b,c)
            self.k1.clear()
            self.k2.clear()
            self.k3.clear()
    def DELETE(self):
        if self.k1.text()!="":
            a=int(self.k1.text())
            self.k.execute("DELETE FROM meva WHERE id=?",(a,))
            self.con.commit()
            self.k1.clear()
            self.k2.clear()
            self.k3.clear()
    def UPDATE(self):
        in1=self.k1.text()
        if self.v2.isChecked():
            a=self.k2.text()
            self.k.execute("UPDATE meva SET name=? WHERE name=?",(in1,a))
        if self.v3.isChecked():
            a=self.k3.text()
            self.k.execute("UPDATE meva SET price=? WHERE price=?",(float(in1),a))
        self.con.commit()
        self.k1.clear()
        self.k2.clear()
        self.k3.clear()
    def SEARCH(self):
        if self.v1.isChecked():
            text=int(self.s.text())
            self.k.execute("SELECT * FROM meva WHERE id=?",(text,))
            ls=self.k.fetchall()
        if self.v2.isChecked():
            text=self.s.text()
            self.k.execute("SELECT * FROM meva WHERE name=?",(text,))
            ls=self.k.fetchall()
        if self.v3.isChecked():
            text=float(self.s.text())
            self.k.execute("SELECT * FROM meva WHERE price=?",(text,))
            ls=self.k.fetchall()
        self.printf.setRowCount(len(ls))

        for i in range(len(ls)):
            self.printf.setItem(i,0,QTableWidgetItem(str(ls[i][0])))
            self.printf.setItem(i,1,QTableWidgetItem(ls[i][1]))
            self.printf.setItem(i,2,QTableWidgetItem(str(ls[i][2])))
        self.s.clear()
    def create(self):
        self.k.execute('''CREATE TABLE IF NOT EXISTS meva
                          (id NUMERIC,name TEXT,price REAL,
                          PRIMARY KEY(id))''')
        self.con.commit()
    def insert(self,a,b,c):
        self.k.execute('''INSERT INTO meva VALUES(?,?,?)''',(a,b,c))
        self.con.commit()
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())
oyna.con.close()
