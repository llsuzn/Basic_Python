# 그리드 레이아웃
# https://wikidocs.net/21946
import sys
from PyQt5.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title'),0, 0) # row : 0, col : 0       
        grid.addWidget(QLabel('Author'),1, 0) # row : 1, col : 0      
        grid.addWidget(QLabel('review'),2, 0) # row : 2, col : 0 

        grid.addWidget(QLineEdit(),0, 1) # 0행 1열
        grid.addWidget(QLineEdit(),1, 1) # 1행 1열
        grid.addWidget(QTextEdit(),2, 1) # 2행 1열

        btnOK = QPushButton('OK')
        btnCancle = QPushButton('Cancle')
        grid.addWidget(btnOK,3, 1)
        grid.addWidget(btnCancle,4, 1)


        # 필수 설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())