import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

from_class = uic.loadUiType("main05.ui")[0]
class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #this가 상속받은곳에 없으면 부모를 찾아감
        
        self.btn1.clicked.connect(self.f_click)
        
        
    def f_click(self):
        num1 = int(self.lineEdit_1.text())
        num2 = int(self.lineEdit_2.text())
        
        self.lineEdit_3.setText(str(num1*num2))
          

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()