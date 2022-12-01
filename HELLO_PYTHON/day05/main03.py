import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

from_class = uic.loadUiType("main03.ui")[0]
class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #this가 상속받은곳에 없으면 부모를 찾아감
        
        self.btn1.clicked.connect(self.f_click)
        
        
    def f_click(self):
        lotto = list(range(1,46))        
        random.shuffle(lotto)        
        
        for i in range(0,6):
            le = self.findChild(QLineEdit, "lineEdit_"+str(i+1))
            le.setText(str(lotto[i]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()