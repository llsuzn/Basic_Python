# 레이아웃 절대적 배치
# https://wikidocs.net/21944
import sys
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1',self)
        label1.move(20,20)
        label2 = QLabel('Label2',self)
        label2.move(20,60)

        btn1 = QPushButton('Button1',self)
        btn1.move(80,13)
        btn2 = QPushButton('Button2',self)
        btn2.move(80,53)

        # 필수 설정
        self.setWindowTitle('절대 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())