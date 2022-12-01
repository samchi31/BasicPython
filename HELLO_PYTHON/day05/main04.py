import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

from_class = uic.loadUiType("main04.ui")[0]
class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #this가 상속받은곳에 없으면 부모를 찾아감
        
        self.btn1.clicked.connect(self.f_click)
        
        
    def f_click(self):
        com=""
        rnd = random.random()
        if rnd > 0.5 :
            com = "짝"
        else:
            com = "홀"
        self.lineEdit_2.setText(com)
        me = self.lineEdit_1.text()
        if me == com:
            self.lineEdit_3.setText("이김")
        else :
            self.lineEdit_3.setText("짐")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()