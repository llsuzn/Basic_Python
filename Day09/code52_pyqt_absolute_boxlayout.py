# 박스 레이아웃 배치
# https://wikidocs.net/21945
import sys
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOK = QPushButton('OK')
        btnCancle = QPushButton('Cancle')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btnOK)
        hbox.addWidget(btnCancle)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
    
        self.setLayout(vbox)        

        # 필수 설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())