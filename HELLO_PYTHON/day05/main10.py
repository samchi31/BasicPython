import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

from_class = uic.loadUiType("main10.ui")[0]
class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #this가 상속받은곳에 없으면 부모를 찾아감
        
        self.com = self.makeRandom()
        
        self.btn.clicked.connect(self.f_click)
  
    
    def f_click(self):
        input = self.le.text()
        
        ballCnt = 0
        strikeCnt = 0
        
        for ch in self.com:
            if ch in input:
                if(self.com.index(ch)==input.index(ch)):
                    strikeCnt+=1
                else:
                    ballCnt+=1
        

        result = ""
        
        if strikeCnt == 3 :
            self.popup()
            result=" com: " + ''.join(self.com)
        elif ballCnt == 0 and strikeCnt==0 :
            result = "3 Out\n"
        else :
            result = "{} Ball, {} Strike\n".format(ballCnt, strikeCnt) 
        self.pte.appendPlainText("{} : {} Strike\n".format(input,result))
        
    def popup(self):
        QMessageBox.question(None,'축하축하', '정답', QMessageBox.Yes, QMessageBox.NoButton)
        
        
    def makeRandom(self):
        arr = ['0','1','2','3','4','5','6','7','8','9']
        random.shuffle(arr)
        return arr[0:3]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()