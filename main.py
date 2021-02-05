import os, sys, json, socket, mainUi
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QFileDialog, QRadioButton, QButtonGroup
class simpQRTool(QtWidgets.QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self, parent=None):
        #Initialize, Nothing to say
        super(simpQRTool, self).__init__(parent)
        self.systemPlatform = sys.platform #Get current system POSIX or Windows or sth else
        self.setupUi(self)
        self.actionExit.triggered.connect(self.exit)
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
        self.modeTextToQR.toggled.connect(self.modeEncode)
        self.encodingUnicode8.toggled.connect(self.encodeModeUni)
        self.encodingAscii.toggled.connect(self.encodeModeAscii)
        self.encodingShift.toggled.connect(self.encodeModeShift)
        self.res172.toggled.connect(self.resSet172)
        self.res480.toggled.connect(self.resSet480)
        self.res720.toggled.connect(self.resSet720)
        self.mainExec.clicked.connect(self.convertTrigger)
        self.importExec.clicked.connect(self.importTrigger)
        self.exportExec.clicked.connect(self.exportMain)
        self.actionExport.triggered.connect(self.exportMain)

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

    def exit(self):
        self.infoOutput(logs='Exit triggered.', terminal=True, statBar=False, statBarTime=0)
        raise SystemExit
#Use to handle mode switch
    def modeDecode(self):
        #Disable all widgets that wont need
        radioButton = self.sender()
        if radioButton.isChecked():    
            self.currentMode = "Q2T"
            #self.mainExec.setEnabled(False)
            self.exportExec.setEnabled(False)
            self.encodingUnicode8.setEnabled(False)
            self.encodingAscii.setEnabled(False)
            self.encodingShift.setEnabled(False)
            self.res172.setEnabled(False)
            self.res480.setEnabled(False)
            self.res720.setEnabled(False)
#Same as up
    def modeEncode(self):
        #Enable all stuff incase some one select "QR to Text" before
        #self.mainExec.setEnabled(True)
        radioButton = self.sender()
        if radioButton.isChecked():
            self.currentMode = "T2Q"
            self.exportExec.setEnabled(True)
            self.encodingShift.setEnabled(True)
            self.encodingUnicode8.setEnabled(True)
            self.encodingAscii.setEnabled(True)
            self.res172.setEnabled(True)
            self.res480.setEnabled(True)
            self.res720.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    form = simpQRTool()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()