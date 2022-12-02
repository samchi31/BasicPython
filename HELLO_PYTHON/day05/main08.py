import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

from_class = uic.loadUiType("main08.ui")[0]
class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #this가 상속받은곳에 없으면 부모를 찾아감
        
        self.btn1.clicked.connect(self.f_click)
        
    def f_click(self):
        start = int(self.le_1.text())
        last = int(self.le_2.text())
        
        result = ""
        for i in range(start,last+1):
            for j in range(0,i):
                result+="*"
            result+="\n"
        self.pte.setPlainText(result)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()