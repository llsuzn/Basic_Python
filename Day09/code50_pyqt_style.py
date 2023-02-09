# 스타일

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스타일 설정
        lbl_red = QLabel('Red') # QLabel 클래스를 이용해서 라벨 위젯을 만듭니다.
        lbl_red.setStyleSheet("color : red;"
                              "border-style : solid;"
                              "border-width : 2px;"
                              "border-color : #FA8072;"
                              "border-radius : 5px")

        lbl_green = QLabel('Green')
        lbl_green.setStyleSheet("color : green;"
                              "border-style : dashed;"
                              "border-width : 5px;"
                              "border-color : #7FFFD4;"
                              "border-radius : 5px")


        # QVBoxLayout 세로로 / QHBoxLayout가로로 위치
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(lbl_red)
        hbox.addWidget(lbl_green)
        hbox.addStretch(1)
        
        vbox = QVBoxLayout() # 세로 구분짓는 레이아웃
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox) # 수직 박스의 창을 메인 레이아웃으로 설정



        # 기본설정 - 사이즈, show 필수!!
        self.setWindowTitle('스타일 지정')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())