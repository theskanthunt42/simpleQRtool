# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 240)
        MainWindow.setMinimumSize(QtCore.QSize(460, 240))
        MainWindow.setMaximumSize(QtCore.QSize(480, 240))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(260, 30, 172, 172))
        self.graphicsView.setObjectName("graphicsView")
        self.textBox = QtWidgets.QTextEdit(self.centralwidget)
        self.textBox.setGeometry(QtCore.QRect(10, 30, 151, 71))
        self.textBox.setObjectName("textBox")
        self.mainExec = QtWidgets.QPushButton(self.centralwidget)
        self.mainExec.setGeometry(QtCore.QRect(170, 30, 75, 23))
        self.mainExec.setObjectName("mainExec")
        self.modeTextToQR = QtWidgets.QRadioButton(self.centralwidget)
        self.modeTextToQR.setGeometry(QtCore.QRect(170, 90, 91, 18))
        self.modeTextToQR.setChecked(False)
        self.modeTextToQR.setObjectName("modeTextToQR")
        self.modeQRToText = QtWidgets.QRadioButton(self.centralwidget)
        self.modeQRToText.setGeometry(QtCore.QRect(170, 110, 91, 18))
        self.modeQRToText.setObjectName("modeQRToText")
        self.labelShow_TextBox = QtWidgets.QLabel(self.centralwidget)
        self.labelShow_TextBox.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.labelShow_TextBox.setObjectName("labelShow_TextBox")
        self.labelShow_QR = QtWidgets.QLabel(self.centralwidget)
        self.labelShow_QR.setGeometry(QtCore.QRect(260, 10, 71, 16))
        self.labelShow_QR.setObjectName("labelShow_QR")
        self.labelShow_Encoding = QtWidgets.QLabel(self.centralwidget)
        self.labelShow_Encoding.setGeometry(QtCore.QRect(10, 110, 61, 16))
        self.labelShow_Encoding.setObjectName("labelShow_Encoding")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 110, 20, 91))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.encodingUnicode8 = QtWidgets.QRadioButton(self.centralwidget)
        self.encodingUnicode8.setGeometry(QtCore.QRect(10, 130, 71, 18))
        self.encodingUnicode8.setObjectName("encodingUnicode8")
        self.encodingAscii = QtWidgets.QRadioButton(self.centralwidget)
        self.encodingAscii.setGeometry(QtCore.QRect(10, 150, 71, 18))
        self.encodingAscii.setObjectName("encodingAscii")
        self.encodingShift = QtWidgets.QRadioButton(self.centralwidget)
        self.encodingShift.setGeometry(QtCore.QRect(10, 170, 71, 18))
        self.encodingShift.setObjectName("encodingShift")
        self.labelShow_Res = QtWidgets.QLabel(self.centralwidget)
        self.labelShow_Res.setGeometry(QtCore.QRect(90, 110, 71, 16))
        self.labelShow_Res.setObjectName("labelShow_Res")
        self.res172 = QtWidgets.QRadioButton(self.centralwidget)
        self.res172.setGeometry(QtCore.QRect(90, 130, 71, 18))
        self.res172.setObjectName("res172")
        self.res480 = QtWidgets.QRadioButton(self.centralwidget)
        self.res480.setGeometry(QtCore.QRect(90, 150, 71, 18))
        self.res480.setObjectName("res480")
        self.res720 = QtWidgets.QRadioButton(self.centralwidget)
        self.res720.setGeometry(QtCore.QRect(90, 170, 71, 18))
        self.res720.setObjectName("res720")
        self.exportExec = QtWidgets.QPushButton(self.centralwidget)
        self.exportExec.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.exportExec.setObjectName("exportExec")
        self.importExec = QtWidgets.QPushButton(self.centralwidget)
        self.importExec.setGeometry(QtCore.QRect(170, 60, 75, 23))
        self.importExec.setObjectName("importExec")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 18))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFiles.addAction(self.actionExit)
        self.menuFiles.addAction(self.actionExport)
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR Code En/Decoder"))
        self.mainExec.setText(_translate("MainWindow", "Convert"))
        self.modeTextToQR.setText(_translate("MainWindow", "Text to QR"))
        self.modeQRToText.setText(_translate("MainWindow", "QR to Text"))
        self.labelShow_TextBox.setText(_translate("MainWindow", "Text box(In & Out)"))
        self.labelShow_QR.setText(_translate("MainWindow", "QR Code"))
        self.labelShow_Encoding.setText(_translate("MainWindow", "Encoding"))
        self.encodingUnicode8.setText(_translate("MainWindow", "UTF-8"))
        self.encodingAscii.setText(_translate("MainWindow", "ASCII"))
        self.encodingShift.setText(_translate("MainWindow", "Shift JIS"))
        self.labelShow_Res.setText(_translate("MainWindow", "Resolution"))
        self.res172.setText(_translate("MainWindow", "172 * 172"))
        self.res480.setText(_translate("MainWindow", "480 * 480"))
        self.res720.setText(_translate("MainWindow", "720 * 720"))
        self.exportExec.setText(_translate("MainWindow", "Export"))
        self.importExec.setText(_translate("MainWindow", "Import"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.actionExport.setText(_translate("MainWindow", "Export to PNG"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
