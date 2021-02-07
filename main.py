import os, sys, json, socket, mainUi, qrcode
#from qrtools.qrtools import QR 
from PIL import Image
import pyzbar.pyzbar as QR
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QFileDialog, QRadioButton, QButtonGroup
from PyQt5.QtGui import QPixmap
class simpQRTool(QtWidgets.QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self, parent=None):
        #Initialize, Nothing to say
        super(simpQRTool, self).__init__(parent)
        self.systemPlatform = sys.platform #Get current system POSIX or Windows or sth else
        self.setupUi(self)
        self.curPath = os.getcwd()
        self.osSep = os.sep
        self.fullFilePath = ''
        self.allLogs =''
        self.textEncoding = 'utf-8'
        self.fileImportStats = False
        self.modeAuto = True
        self.actionExit.triggered.connect(self.exit)
        self.sizeOfImage = 1
        #self.encodingUnicode8.setChecked(True) #Default value
        self.buttonGroupMode = QButtonGroup() #Create groups for radio buttons
        self.buttonGroupEncoding = QButtonGroup()
        self.buttonGroupSize = QButtonGroup()
        self.buttonGroupMode.addButton(self.modeQRToText) #Add button to their groups
        self.buttonGroupMode.addButton(self.modeTextToQR)
        self.buttonGroupEncoding.addButton(self.encodingUnicode8)
        self.buttonGroupEncoding.addButton(self.encodingAscii)
        self.buttonGroupEncoding.addButton(self.encodingShift)
        self.buttonGroupSize.addButton(self.sizeAutoButton)
        self.buttonGroupSize.addButton(self.sizeManualButton)
        self.sizeSlider.setEnabled(False)#Default value
        self.sizeAutoButton.setChecked(True)
        self.modeTextToQR.setChecked(True)
        self.encodingUnicode8.setChecked(True)
        self.modeQRToText.toggled.connect(self.modeDecode) #Toggle connect
        self.modeTextToQR.toggled.connect(self.modeEncode)
        self.encodingUnicode8.toggled.connect(self.encodeModeUni)
        self.encodingAscii.toggled.connect(self.encodeModeAscii)
        self.encodingShift.toggled.connect(self.encodeModeShift)
        self.mainExec.clicked.connect(self.convertTrigger)
        self.importExec.clicked.connect(self.importTrigger)
        self.exportExec.clicked.connect(self.exportMain)
        self.actionExport.triggered.connect(self.exportMain)
        self.sizeAutoButton.toggled.connect(self.autoSetMode)
        self.sizeManualButton.toggled.connect(self.manualSetMode)
        self.sizeSlider.valueChanged.connect(self.sliderValueChanging)

    def mainDecoder(self, filePath):
        if self.fileImportStats:
            try:
                data = QR.decode(Image.open(filePath))
                self.pixmapLabel.setPixmap(QPixmap(filePath))
                print(data[0].data.decode())
                self.textBox.setText(data[0].data.decode())
            except SystemError:
                self.infoOutput("Can't decode QR code!", True, True, 1000)
        else:
            self.infoOutput("Please import the image first.", True, True, 1000)
        return None

    def exportMain(self):
        if self.genStat:
            fileName = self.textInBox[:7]
            if self.systemPlatform == 'linux' or 'linux2' or 'darwin' or 'freebsd' or 'openbsd' or 'macos':
                try:
                    os.system(f'cp .tmp.png {self.curPath}/Output/{fileName}.png')
                    self.infoOutput(f"PNG exported to {self.curPath}/Output/{fileName}.png", True, True, 2000)
                except SystemError:
                    self.infoOutput("Can't copy file to Output.", True, True, 1500)
            elif self.systemPlatform == 'win32' or 'win64' or 'cygwin' or 'msys':
                try:
                    os.system(f'copy .temp.png {self.curPath}\\Output\\{fileName}.png')
                    self.infoOutput(f"PNG exported to {self.curPath}\\Output\\{fileName}.png", True, True, 2000)
                except SystemError:
                    self.infoOutput("Can't copy file to Output.", True, True, 1500)
            else:
                self.infoOutput("Cant copy file to Output.", True, True, 1000)
        else:
            self.infoOutput("Please generate the QR code first.", True, True, 1000)
        return None

    def mainEncoder(self, text):
        size = None
        with open('config.json') as f:
            settings = json.load(f)
        if self.modeAuto != True:
            size = None
        else:
            size = self.sizeSlider.value()
        qrObject = qrcode.QRCode(version=size, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        try:
            qrObject.add_data(text.encode(self.textEncoding))
        except SystemError:
            self.infoOutput(logs='Error when adding text to decoder.', terminal=True, statBar=True, statBarTime=2000)
        try:
            qrObject.make(fit=True)
        except SystemError:
            self.infoOutput(logs='Error when generating QR Code.', terminal=True, statBar=True, statBarTime=2000)
        imageObject = qrObject.make_image(fill_color=settings['color'], back_color=settings['background_color'])
        imageObject.save('.tmp.png')
        self.pixmapLabel.setPixmap(QPixmap('.tmp.png'))
        self.genStat = True

    def convertTrigger(self):
        self.textInBox = self.textBox.toPlainText()
        if self.textInBox != '' or None:
            self.mainEncoder(self.textInBox)
        else:
            self.infoOutput(logs='Error! Please fill some text into the box!', terminal=True, statBar=True, statBarTime=1500)

    def sliderValueChanging(self, value):
        self.sizeOfImage = value
        self.infoOutput(logs=f'Size changed to {self.sizeOfImage}', terminal=True, statBar=True, statBarTime=1000)
        return None

    def autoSetMode(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.modeAuto = True
            self.sizeSlider.setEnabled(False)
        return None

    def manualSetMode(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.modeAuto = False
            self.sizeSlider.setEnabled(True)
        return None


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
        os.remove(f'{self.curPath}{self.osSep}.tmp.png')
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
            self.sizeAutoButton.setEnabled(False)
            self.sizeManualButton.setEnabled(False)
            self.sizeSlider.setEnabled(False)
        return None
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
            self.sizeAutoButton.setEnabled(True)
            self.sizeManualButton.setEnabled(True)
            self.sizeSlider.setEnabled(True)
        return None
    #Text encoding
    def encodeModeUni(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.textEncoding = 'utf-8'
        return None
    
    def encodeModeAscii(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.textEncoding = 'ascii'
        return None
    
    def encodeModeShift(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.textEncoding = 'shift-jis'
        return None
    #Import files using QFileDialog
    def importTrigger(self):
        self.fileDialog = QFileDialog.getOpenFileName(self, 'Open file', self.curPath, "PNG files (*.png)")
        self.fullFilePath = self.fileDialog[0]
        #self.fileName = self.fullFilePath.split(os.sep)[len(self.fullFilePath) -1]
        #Just figure out I only need the path to the file...
        self.fileImportStats = True
        self.infoOutput(f'Selected file: {self.fullFilePath}', terminal=True, statBar=True, statBarTime=1500)
        self.mainDecoder(self.fullFilePath)
        return None
    

def main():
    app = QApplication(sys.argv)
    form = simpQRTool()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()