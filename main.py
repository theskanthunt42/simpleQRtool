import os, sys, json, socket, mainUi
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QFileDialog, QRadioButton, QButtonGroup
class simpQRTool(QtWidgets.QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self, parent=None):
        #Initialize, Nothing to say
        super(simpQRTool, self).__init__(parent)
        self.systemPlatform = sys.platform #Get current system POSIX or Windows or sth else
        self.setupUi(self)
        self.encodingUnicode8.setChecked(True) #Default value
        self.res172.setChecked(True)
        self.modeTextToQR.setChecked(True)
        self.buttonGroupMode = QButtonGroup() #Create groups for radio buttons
        self.buttonGroupEncoding = QButtonGroup()
        self.buttonGroupRes = QButtonGroup()
        self.buttonGroupMode.addButton(self.modeQRToText) #Add button to their groups
        self.buttonGroupMode.addButton(self.modeTextToQR)
        self.buttonGroupEncoding.addButton(self.encodingUnicode8)
        self.buttonGroupEncoding.addButton(self.encodingAscii)
        self.buttonGroupEncoding.addButton(self.encodingShift)
        self.buttonGroupRes.addButton(self.res172)
        self.buttonGroupRes.addButton(self.res480)
        self.buttonGroupRes.addButton(self.res720)
        self.modeQRToText.toggled.connect(self.modeDecode) #Toggle connect
        self.modeTextToQR.toggle.connect(self.modeEncode)
        self.encodingUnicode8.toggled.connect(self.encodeModeUni)
        self.encodingAscii.toggled.connect(self.encodeModeAscii)
        self.encodingShift.toggled.connect(self.encodeModeShift)
        self.res172.toggled.connect(self.resSet172)
        self.res480.toggled.connect(self.resSet480)
        self.res720.toggled.connect(self.resSet720)

#This function below is use to output infomations to Terminal or the statubar of the GUI
    def infoOutput(self, logs, terminal, statBar, statBarTime):
        self.allLogs = self.allLogs + str(logs) + '\n'
        if terminal == True:
            print(logs)
        else:
            pass
        if statBar == True and statBarTime != None or 0:
            self.statusbar.showMessage(logs, statBarTime)
        else:
            pass

        