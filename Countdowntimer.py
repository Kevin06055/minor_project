
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 600)
        MainWindow.setStyleSheet("background-color: rgb(16, 16, 16);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.start=0
        self.count=0

        #Start functiom
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(10, 210, 261, 171))
        self.Start.setMouseTracking(True)
        self.Start.setAutoFillBackground(False)
        self.Start.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 127);\n"
"selection-background-color: rgb(255, 255, 127);\n"
"font: 17pt \"MS Shell Dlg 2\";\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 25px;\n"
"border-color: blue;\n"
"padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(255, 20, 83);\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.Start.setCheckable(False)
        self.Start.setAutoDefault(True)
        self.Start.setDefault(False)
        self.Start.setFlat(False)
        self.Start.setObjectName("Start")
        self.Start.clicked.connect(self.start_action)



        #label Function
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 771, 181))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 72pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")





        #pause funtion
        self.Pause = QtWidgets.QPushButton(self.centralwidget)
        self.Pause.setGeometry(QtCore.QRect(550, 190, 231, 91))
        self.Pause.setMouseTracking(True)
        self.Pause.setAutoFillBackground(False)
        self.Pause.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 127);\n"
"selection-background-color: rgb(255, 255, 127);\n"
"font: 17pt \"MS Shell Dlg 2\";\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 25px;\n"
"border-color: blue;\n"
"padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(255, 20, 83);\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.Pause.setCheckable(False)
        self.Pause.setAutoDefault(True)
        self.Pause.setDefault(False)
        self.Pause.setFlat(False)
        self.Pause.setObjectName("Pause")
        self.Pause.clicked.connect(self.pause_action)



        #set timer function
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(100)
        self.set_timer = QtWidgets.QPushButton(self.centralwidget)
        self.set_timer.setGeometry(QtCore.QRect(280, 210, 261, 171))
        self.set_timer.setMouseTracking(True)
        self.set_timer.setAutoFillBackground(False)
        self.set_timer.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 127);\n"
"selection-background-color: rgb(255, 255, 127);\n"
"font: 17pt \"MS Shell Dlg 2\";\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 25px;\n"
"border-color: blue;\n"
"padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(255, 20, 83);\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.set_timer.setCheckable(False)
        self.set_timer.setAutoDefault(True)
        self.set_timer.setDefault(False)
        self.set_timer.setFlat(False)
        self.set_timer.setObjectName("set_timer")
        self.set_timer.clicked.connect(self.get_seconds)




        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 400, 781, 141))
        self.plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.plainTextEdit.setObjectName("plainTextEdit")




        #stop function
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(550, 290, 231, 91))
        self.Stop.setMouseTracking(True)
        self.Stop.setAutoFillBackground(False)
        self.Stop.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 255, 127);\n"
"selection-background-color: rgb(255, 255, 127);\n"
"font: 17pt \"MS Shell Dlg 2\";\n"
"border-style: outset;\n"
"border-width: 0px;\n"
"border-radius: 25px;\n"
"border-color: blue;\n"
"padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(255, 20, 83);\n"
"    \n"
"    background-color: rgb(255, 255, 0);\n"
"}\n"
"")
        self.Stop.setCheckable(False)
        self.Stop.setAutoDefault(True)
        self.Stop.setDefault(False)
        self.Stop.setFlat(False)
        self.Stop.setObjectName("Stop")
        self.Stop.clicked.connect(self.stop_action)






        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # method called by timer

    def showTime(self):

        # checking if flag is true
        if self.start:
            # incrementing the counter
            self.count -= 1

            # timer is completed
            if self.count == 0:
                # making flag false
                self.start = False

                # setting text to the label
                self.label.setText("Completed !!!! ")

        if self.start:
            # getting text from count
            text = str(self.count / 10) + " s"

            # showing text
            self.label.setText(text)

        # method called by the push button

    def get_seconds(self):

        # making flag false
        self.start = False

        # getting seconds and flag
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')

        # if flag is true
        if done:
            # changing the value of count
            self.count = second * 10

            # setting text to the label
            self.label.setText(str(second))

    def start_action(self):
        # making flag true
        self.start = True

        # count = 0
        if self.count == 0:
            self.start = False

    def pause_action(self):

        # making flag false
        self.start = False

    def stop_action(self):

        # making flag false
        self.start = False

        # setting count value to 0
        self.count = 0

        # setting label text
        self.label.setText("RESET")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start.setText(_translate("MainWindow", "Start/Resume"))
        self.Start.setShortcut(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">00:00:00</p></body></html>"))
        self.Pause.setText(_translate("MainWindow", "Pause"))
        self.Pause.setShortcut(_translate("MainWindow", "Space", " p"))
        self.set_timer.setText(_translate("MainWindow", "Set timer"))
        self.set_timer.setShortcut(_translate("MainWindow", "X"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Start/Resume = Press Enter Key\n"
"\n"
"Set Timer = Press X\n"
"\n"
"Pause = Press Space Key\n"
""))
        self.Stop.setText(_translate("MainWindow", "Stop"))
        self.Stop.setShortcut(_translate("MainWindow", "Space", " p"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
