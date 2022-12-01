import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("main01.ui")[0]
class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #this가 상속받은곳에 없으면 부모를 찾아감
        
        self.btn1.clicked.connect(self.f_click)
        
        
    def f_click(self):
        self.lineEdit.setText(str(int(self.lineEdit.text())*2))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()