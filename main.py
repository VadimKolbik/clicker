import design
import mouse, time, sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTimeEdit, QCheckBox
from PyQt6.QtCore import QThread, Qt, QTimer, QTime
from PyQt6.QtGui import QIcon

class ClickerRun(QThread):
    def __init__(self, mainwindow, parent=None):
        super(ClickerRun, self).__init__()
        self.mainwindow = mainwindow
    
    def run(self):
        start = time.time()
        working_time = self.mainwindow.spinBox_sec.value() + self.mainwindow.spinBox_min.value()*60 + self.mainwindow.spinBox_hour.value()*3600
        while self.mainwindow.running and time.time() - start < working_time:
            if self.mainwindow.radiobutton_active_click.isChecked():
                mouse.click('left')
            else:
                pass
            x, y = mouse.get_position()
            self.mainwindow.lineEdit.setText(str(x))
            self.mainwindow.lineEdit_2.setText(str(y))
            time.sleep(self.mainwindow.interval.value())
        else: 
            self.mainwindow.stop_clicking()


class ClickerApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QIcon(scriptDir + os.path.sep + 'icon.png'))
        
        self.pushButton.clicked.connect(self.run_clicking)
        self.pushButton_2.clicked.connect(self.stop_clicking)
        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton.setShortcut('1')
        self.pushButton_2.setShortcut('2')
        self.pushButton_3.setShortcut('Esc')
        self.pushButton.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255)} QPushButton:hover { background-color: rgb(200, 200, 200)}")
        self.pushButton_2.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255)} QPushButton:hover { background-color: rgb(200, 200, 200)}")
        self.pushButton_3.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255)} QPushButton:hover { background-color: rgb(200, 200, 200)}")
        self.interval.setValue(1)
        self.interval.setSingleStep(0.1)
        self.spinBox_min.setMaximum(59)
        self.spinBox_sec.setMaximum(59)
        self.spinBox_sec.setValue(10)
        self.running = True

        self.radiobutton_active_click = QCheckBox('Клик активен', parent=self.widget)
        self.radiobutton_OnTopHint = QCheckBox('Приложение поверх всех окон', parent=self.widget)
        self.gridLayout.addWidget(self.radiobutton_active_click, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.radiobutton_OnTopHint, 4, 1, 1, 2)
        self.radiobutton_OnTopHint.setChecked(True)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.time = QTime(0, 0, 0)
        self.clicker_class = ClickerRun(self)
    
    def run_clicking(self):
        print(self.radiobutton_OnTopHint.isChecked())
        if self.radiobutton_OnTopHint.isChecked():
            self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(Qt.WindowType.Window)
            
        self.pushButton.setStyleSheet("QPushButton { background-color: rgb(88, 184, 109)} QPushButton:hover { background-color: rgb(108, 217, 132)}")
        self.pushButton_2.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255)} QPushButton:hover { background-color: rgb(200, 200, 200)}")
        self.running = True
        self.timer.start(1000)
        self.clicker_class.start()
    
    def stop_clicking(self):
        self.pushButton.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255)} QPushButton:hover { background-color: rgb(200, 200, 200)}")
        self.pushButton_2.setStyleSheet("QPushButton { background-color: rgb(201, 44, 55)} QPushButton:hover { background-color: rgb(204, 92, 99)}")
        self.running = False
        self.timer.stop()

    def exit(self):
        sys.exit()
    
    def time(self):
        self.time = self.time.addSecs(1)
        self.working_time.display(self.time.toString("hh:mm:ss"))



def main():
    app = QApplication(sys.argv)
    clicker = ClickerApp()
    clicker.show()
    app.exec()


if __name__ == '__main__':
    main()