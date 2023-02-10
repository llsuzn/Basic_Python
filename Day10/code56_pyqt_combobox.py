# combobox https://wikidocs.net/21940
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblOption = QLabel('CHECK ',self)
        self.lblOption.move(30,20)

        CBOption = QComboBox(self)
        CBOption.addItem('Option1')
        CBOption.addItem('Option2')
        CBOption.addItem('Option3')
        CBOption.addItem('Option4')
        CBOption.addItem('Option5')
        CBOption.move(20,40)

        CBOption.activated[str].connect(self.onActivate) # onActivate : 슬롯 함수

        # 필수 설정
        self.setWindowTitle('콤보박스')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onActivate(self,text):
        self.lblOption.setText('선택값 : ' + text)
        self.lblOption.adjustSize() # 글자수 만큼 라벨 넓이를 조정

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())