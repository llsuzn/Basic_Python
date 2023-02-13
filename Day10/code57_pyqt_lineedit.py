# 라인에디트 - textbox https://wikidocs.net/33806
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblresult = QLabel(self)
        self.lblresult.move(20,20)
        
        txtInput = QLineEdit(self)
        txtInput.setEchoMode(2) #  '쓰기 전용' 영역(비밀번호 쓸 때 유용함)
        txtInput.move(20,40)
        txtInput.textChanged[str].connect(self.onChanged) # onChanged : 슬롯함수 
        self.lblresult.setText('비밀번호')

        # 필수설정
        self.setWindowTitle('라인 에디트')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onChanged(self,text):
        self.lblresult.setText('password : ' + text)
        self.lblresult.adjustSize() #라벨사이즈 자동

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())