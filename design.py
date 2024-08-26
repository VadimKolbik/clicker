# Form implementation generated from reading ui file 'app_clicker.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(406, 221)
        MainWindow.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(5, 5, 396, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 2, 1, 1)
        self.label_curr_work_time = QtWidgets.QLabel(parent=self.widget)
        self.label_curr_work_time.setObjectName("label_curr_work_time")
        self.gridLayout.addWidget(self.label_curr_work_time, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 2)
        self.label_clicker_time = QtWidgets.QLabel(parent=self.widget)
        self.label_clicker_time.setObjectName("label_clicker_time")
        self.gridLayout.addWidget(self.label_clicker_time, 1, 0, 1, 1)
        self.interval = QtWidgets.QDoubleSpinBox(parent=self.widget)
        self.interval.setObjectName("interval")
        self.gridLayout.addWidget(self.interval, 0, 1, 1, 2)
        self.label_position = QtWidgets.QLabel(parent=self.widget)
        self.label_position.setObjectName("label_position")
        self.gridLayout.addWidget(self.label_position, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox_hour = QtWidgets.QSpinBox(parent=self.widget)
        self.spinBox_hour.setObjectName("spinBox_hour")
        self.horizontalLayout.addWidget(self.spinBox_hour)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_min = QtWidgets.QSpinBox(parent=self.widget)
        self.spinBox_min.setObjectName("spinBox_min")
        self.horizontalLayout.addWidget(self.spinBox_min)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.spinBox_sec = QtWidgets.QSpinBox(parent=self.widget)
        self.spinBox_sec.setObjectName("spinBox_sec")
        self.horizontalLayout.addWidget(self.spinBox_sec)
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 2)
        self.working_time = QtWidgets.QLCDNumber(parent=self.widget)
        self.working_time.setObjectName("working_time")
        self.gridLayout.addWidget(self.working_time, 3, 1, 1, 2)
        self.label_interval = QtWidgets.QLabel(parent=self.widget)
        self.label_interval.setObjectName("label_interval")
        self.gridLayout.addWidget(self.label_interval, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoClicker"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit (Esc)"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop (2)"))
        self.label_curr_work_time.setText(_translate("MainWindow", "Текущее время работы, сек:"))
        self.pushButton.setText(_translate("MainWindow", "Start (1)"))
        self.label_6.setText(_translate("MainWindow", "X"))
        self.label_7.setText(_translate("MainWindow", "Y"))
        self.label_clicker_time.setText(_translate("MainWindow", "Задать время работы:"))
        self.label_position.setText(_translate("MainWindow", "Текущая позиция курсора:"))
        self.label_3.setText(_translate("MainWindow", "ч"))
        self.label_4.setText(_translate("MainWindow", "мин"))
        self.label_5.setText(_translate("MainWindow", "сек"))
        self.label_interval.setText(_translate("MainWindow", "Интервал клика, сек:"))
