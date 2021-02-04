import os, sys, json, socket, mainUi
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QAction, QFileDialog, QRadioButton, QButtonGroup
class simpQRTool(QtWidgets.QMainWindow, mainUi.Ui_MainWindow):
    def __init__(self, parent=None):
        super(simpQRTool, self).__init__(parent)
        self.systemPlatform = sys.platform
        self.setupUi(self)
        self.encodingUnicode8.setChecked(True)
        self.res172.setChecked(True)
        self.modeTextToQR.setChecked(True)
        self.buttonGroupMode = QButtonGroup()
        self.buttonGroupEncoding = QButtonGroup()
        self.buttonGroupRes = QButtonGroup()
        self.buttonGroupMode.addButton(self.modeQRToText)
        self.buttonGroupMode.addButton(self.modeTextToQR)
        self.buttonGroupEncoding.addButton(self.encodingUnicode8)
        self.buttonGroupEncoding.addButton(self.encodingAscii)
        self.buttonGroupEncoding.addButton(self.encodingShift)
        self.buttonGroupRes.addButton(self.res172)
        self.buttonGroupRes.addButton(self.res480)
        self.buttonGroupRes.addButton(self.res720)
        