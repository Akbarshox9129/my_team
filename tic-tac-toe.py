from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton,QRadioButton,QMessageBox
from PyQt5.QtGui import QFont
import sys
class Tugma(QPushButton):
    def __init__(self,name,ob,x,y):
        super().__init__(name,ob)
        self.setFont(QFont("Times",40))
        self.setGeometry(x,y,100,100)
    def click(self,fun):
        self.clicked.connect(fun)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,600,600)
        self.begin()
        self.x=""
    def font(self,ob):
        ob.setFont(QFont("Times",40))
    def begin(self):
        self.var1=QRadioButton("X",self)
        self.var2=QRadioButton("O",self)
        self.font(self.var1)
        self.var1.move(20,50)
        self.font(self.var2)
        self.var2.move(100,50)
        self.ok=Tugma("Ok",self,50,150)
        self.ok.click(self.run)
        self.a1=Tugma("",self,50,50)
        self.a2=Tugma("",self,160,50)
        self.a3=Tugma("",self,270,50)
        self.a4=Tugma("",self,50,160)
        self.a5=Tugma("",self,160,160)
        self.a6=Tugma("",self,270,160)
        self.a7=Tugma("",self,50,270)
        self.a8=Tugma("",self,160,270)
        self.a9=Tugma("",self,270,270)
        self.a1.hide()
        self.a2.hide()
        self.a3.hide()
        self.a4.hide()
        self.a5.hide()
        self.a6.hide()
        self.a7.hide()
        self.a8.hide()
        self.a9.hide()
        self.a1.click(self.A1)
        self.a2.click(self.A2)
        self.a3.click(self.A3)
        self.a4.click(self.A4)
        self.a5.click(self.A5)
        self.a6.click(self.A6)
        self.a7.click(self.A7)
        self.a8.click(self.A8)
        self.a9.click(self.A9)
    def run(self):
        if self.var1.isChecked():
            self.x="X"
        if self.var2.isChecked():
            self.x="O"
        self.a1.show()
        self.a2.show()
        self.a3.show()
        self.a4.show()
        self.a5.show()
        self.a6.show()
        self.a7.show()
        self.a8.show()
        self.a9.show()
        self.var1.hide()
        self.var2.hide()
        self.ok.hide()
    def scan(self):
        win=QMessageBox(self)
        win.setWindowTitle("Tic-Tac-Toe")
        if self.a1.text()!="" and self.a1.text()==self.a2.text() and self.a2.text()==self.a3.text():
            win.setText(self.a1.text()+" WINS!!!!!!!!!")
            win.show()
            self.refresh()
        elif self.a1.text()!="" and self.a1.text()==self.a4.text() and self.a4.text()==self.a7.text():
            win.setText(self.a1.text()+" WINS!!!!!!!!!")
            win.show()
            self.refresh()
        elif self.a1.text()!="" and self.a1.text()==self.a5.text() and self.a5.text()==self.a9.text():
            win.setText(self.a1.text()+" WINS!!!!!!!!!")
            win.show()
            self.refresh()
        elif self.a2.text()!="" and self.a2.text()==self.a5.text() and self.a5.text()==self.a8.text():
            win.setText(self.a2.text()+" WINS!!!!!!!!!")
            win.show()
            self.refresh()
        elif self.a3.text()!="" and self.a3.text()==self.a6.text() and self.a6.text()==self.a9.text():
            win.setText(self.a3.text()+" WINS!!!!!!!!!")
            win.show()
            self.refresh()
        elif self.a7.text()!="" and self.a7.text()==self.a8.text() and self.a8.text()==self.a9.text():
            win.setText(self.a7.text()+" WINS!!!!!!!!!")
            win.show()
            self.refresh()
        elif self.a3.text()!="" and self.a3.text()==self.a5.text() and self.a5.text()==self.a7.text():
            win.setText(self.a3.text()+" WINS!!!!!!!!!")
            win.show()
            self.refresh()
        elif self.a4.text()!="" and self.a4.text()==self.a5.text() and self.a5.text()==self.a6.text():
            win.setText(self.a4.text()+" WINS!!!!!!!!!")
            win.show()
            self.refresh()
        elif (self.a1.text()!="" and self.a2.text()!="" and self.a3.text()!="" and
              self.a4.text()!="" and self.a5.text()!="" and self.a6.text()!="" and
              self.a7.text()!="" and self.a8.text()!="" and self.a9.text()!=""):
            win.setText("DRAW!!!!!!!!!")
            win.show()
            self.refresh()
    def refresh(self):
        self.a1.hide()
        self.a2.hide()
        self.a3.hide()
        self.a4.hide()
        self.a5.hide()
        self.a6.hide()
        self.a7.hide()
        self.a8.hide()
        self.a9.hide()
        self.var1.show()
        self.var2.show()
        self.ok.show()
        self.a1.setText("")
        self.a2.setText("")
        self.a3.setText("")
        self.a4.setText("")
        self.a5.setText("")
        self.a6.setText("")
        self.a7.setText("")
        self.a8.setText("")
        self.a9.setText("")
    def A1(self):
        if self.a1.text()=="":
            self.a1.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
    def A2(self):
        if self.a2.text()=="":
            self.a2.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
    def A3(self):
        if self.a3.text()=="":
            self.a3.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
    def A4(self):
        if self.a4.text()=="":
            self.a4.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
    def A5(self):
        if self.a5.text()=="":
            self.a5.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
    def A6(self):
        if self.a6.text()=="":
            self.a6.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
    def A7(self):
        if self.a7.text()=="":
            self.a7.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
    def A8(self):
        if self.a8.text()=="":
            self.a8.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
    def A9(self):
        if self.a9.text()=="":
            self.a9.setText(self.x)
            if self.x=="X":
                self.x="O"
            else:
                self.x="X"
        self.scan()
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())
