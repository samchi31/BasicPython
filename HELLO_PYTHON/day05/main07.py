import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

from_class = uic.loadUiType("main07.ui")[0]
class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #this가 상속받은곳에 없으면 부모를 찾아감
        
        self.btn1.clicked.connect(self.f_click)
        self.le_1.returnPressed.connect(self.f_click)
        
    def f_click(self):
        coms = ["가위", "바위", "보"]
        com = coms[int(random.random()*3)]
        self.le_2.setText(com)
        me = self.le_1.text()
        result=""
        if com == me :
            result = "비김"
        elif (com == "가위" and me == "바위") or (com == "바위" and me == "보") or (com == "보" and me == "가위"):
            result="me 이김"
        else:
            result="com 이김"
        self.le_3.setText(result)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()