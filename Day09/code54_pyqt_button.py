# push button
# https://wikidocs.net/21946
import sys
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1',self) # &B : alt + B => toggle 활성화 설정
        btn1.setCheckable(True) # 버튼 누르면 1 한 번 더 누르면 0
        btn1.toggle()

        btn2 = QPushButton(self) 
        btn2.setText('Button&2') 

        btn3 = QPushButton('Button3',self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)

        # 필수 설정
        self.setWindowTitle('푸시 버튼')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())