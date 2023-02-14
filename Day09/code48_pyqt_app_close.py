# window 창 닫기 앱
# 2023/02/09
# llsuzn
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit',self)
        btn.move(320,170)
        btn.resize(btn.sizeHint())
        # 버튼 툴팁
        btn.setToolTip('program <b>close</b>')
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowIcon(QIcon('./Day09/iot.png'))
        self.setWindowTitle('Quit Button')
        self.setGeometry(1000,200,400,200) #(x,y,w,h) w : 창의 가로 크기 h : 창의 세로 크기
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
