# 창 띄우기
# https://wikidocs.net/21920
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget): #QWidget의 기능을 MyApp에서 사용가능
    pass
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window') # 타이틀 설정
        # self.move(1920-400,1080-200) # 창 위치 설정 (x,y)... (0,0) : 제일 왼쪽
        # self.move(1920//2 - 200,1080//2-100) # 창 위치 정중앙에 위치시키기
        self.resize(400, 200)
        self.show() # 핵심!(창 띄우기)
    
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())