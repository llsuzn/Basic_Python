# https://wikidocs.net/21853 아이콘 넣기 
# https://www.flaticon.com/
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget): #QWidget의 기능을 MyApp에서 사용가능
    pass
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window') # 타이틀 설정
        # 아이콘 추가
        self.setWindowIcon(QIcon('./Day09/iot.png')) 
        self.resize(400, 200)
        self.show() # 핵심!(창 띄우기)
    
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())