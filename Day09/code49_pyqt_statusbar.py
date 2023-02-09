# 날짜와 시간
# https://wikidocs.net/22074
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow ,QPushButton, QAction, qApp, QDesktopWidget # *로 다 포함시켜도 됨
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, QDate, Qt ,QTime

class MyApp(QMainWindow): #QWidget의 기능을 MyApp에서 사용가능
       
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 액션
        actExit = QAction(QIcon('./Day09/exit.png'),'Exit',self)
        actExit.setShortcut('Ctrl+Q')
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit)
        
        actSave = QAction(QIcon('./Day09/save.png'),'Save',self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')
        # actSave.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # Tool bar
        toolbar = self.addToolBar('MainToolBar')  # 툴바 타이틀은 업어도 됨
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)

        # status bar
        # 아이콘 추가
        self.setWindowIcon(QIcon('./Day09/iot.png')) 
        btn = QPushButton('Quit',self)
        btn.move(320,170)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        # 현재 날짜 
        now = QDate.currentDate() 
        # 현재 시간
        time = QTime.currentTime()
        # self.statusBar().showMessage(now.toString('yyyy MM dd dddd'))
        self.statusBar().showMessage(now.toString(Qt.DefaultLocaleShortDate) + ' ' + time.toString())

 

        # GUI 화면 설정
        self.setWindowTitle('Simple Window') # 타이틀 설정
        # self.move(0,0)   self.setCenter()실행되면 쓰레기 코드
        self.resize(400, 200)
        self.setCenter()
        self.show() # 핵심!(창 띄우기)
    
    # 창을 화면의 가운데로
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 사용자 pc 화면 센터 찾는 것
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())