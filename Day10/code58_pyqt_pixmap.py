# pixmap https://wikidocs.net/33768
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('./Day10/cat.png')
        

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblImage_size = QLabel('size : ' + str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblImage_size.setAlignment(Qt.AlignmentFlag.AlignCenter) #Qt.AlignCenter도 가능

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblImage_size)

        self.setLayout(vbox)

        # 필수설정
        self.setWindowTitle('이미지 위젯')
        # self.showFullScreen() # 전체화면...나가기 버튼 안 나옴
        self.setGeometry(700, 100, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())