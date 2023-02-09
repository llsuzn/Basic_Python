# CheckBox https://wikidocs.net/21937
# RadioButton https://wikidocs.net/21938
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 체크박스
        cbShowTitle = QCheckBox('Show Title', self)
        cbShowTitle.move(20,20)
        cbShowTitle.toggle()
        
        # cbShowTitle.setStatusTip

        # 시그널
        # connnect() 매개변수 -> 슬롯함수
        cbShowTitle.stateChanged.connect(self.changeTitle)
        cbKorea = QCheckBox('한국',self)
        cbKorea.move(20, 40)
        cbKorea.stateChanged.connect(self.checkKorea)

        # 라디오 박스
        rbMale = QRadioButton('남성',self)
        rbMale.move(150, 20)
        rbMale.setChecked(True)
        rbFemale = QRadioButton('여성',self)
        rbFemale.move(150, 40)

        # 필수 설정
        self.setWindowTitle('푸시 버튼')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    
    def checkKorea(self,state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('한국인')
        else:
            self.setWindowTitle('한국인이 아닙니다')

    def changeTitle(self,state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('체크박스 체크')
        
            # self.setStatusTip
        
        else:
            self.setWindowTitle('체크박스 체크해제')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())