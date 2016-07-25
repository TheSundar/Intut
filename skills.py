# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skills.ui'
#
# Created: Thu Jun 09 17:33:43 2016
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
import zipfile
import re
import os
import os.path
import xml.etree.ElementTree as ET
from docreader import document_to_text

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1070, 895)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem = QtGui.QSpacerItem(158, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 518, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        spacerItem2 = QtGui.QSpacerItem(488, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_7)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.showdocuments()

        self.designation=[]
        self.skillSet=[]

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_5.setText(_translate("MainWindow", "Designation :", None))
        self.label_6.setText(_translate("MainWindow", "Skills Sets :", None))
        self.label_7.setText("")
        self.pushButton.setText(_translate("MainWindow", "Save", None))
        self.pushButton_2.setText(_translate("MainWindow", "Reset", None))
        self.pushButton_6.setText(_translate("MainWindow", "Previous", None))
        self.pushButton_5.setText(_translate("MainWindow", "Next", None))
		
    def showdocuments(self):
        self.fileName = []
        self.fileCount = 0
        self.currentcount = 0

        self.pushButton.clicked.connect(self.onSave_clicked)
        self.pushButton_6.clicked.connect(self.onPrevbtn_clicked)
        self.pushButton_5.clicked.connect(self.onNextbtn_clicked)

        for i in os.listdir(r'F:\PYTHON\Sundar_work\OurGoal\data\\'):
            try:
                self.fileName.append(r'F:\PYTHON\Sundar_work\OurGoal\data\\'+i)
            except:
                import sys
                print sys.exc_info()
                pass

        self.fileCount = len(self.fileName)
        content = document_to_text(os.path.basename(self.fileName[0]),self.fileName[0])
        self.label_7.setText(str(os.path.basename(self.fileName[0])))
        self.textEdit.setText(content)

    def onPrevbtn_clicked(self):
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

        if self.currentcount >= 0:
            content = document_to_text(os.path.basename(self.fileName[self.currentcount]),self.fileName[self.currentcount])
            self.textEdit.setText(content)
            self.label_7.setText(str(os.path.basename(self.fileName[self.currentcount])))
            self.currentcount = self.currentcount - 1
        else:
            # QtGui.QMessageBox.warning(self, 'Warning', "No Previous Resume !!!")
            pass

    def onNextbtn_clicked(self):
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

        if self.currentcount <= self.fileCount:
            content = document_to_text(os.path.basename(self.fileName[self.currentcount]),self.fileName[self.currentcount])
            self.textEdit.setText(content)
            self.label_7.setText(str(os.path.basename(self.fileName[self.currentcount])))
            self.currentcount = self.currentcount + 1
        else:
            pass
            QtGui.QMessageBox.warning(self, 'Warning', "No Next Resume !!!")

    def onSave_clicked(self):

        self.designation.extend(str(self.lineEdit_4.text()).split(","))

        skill = str(self.lineEdit_5.text()).split(",")
        [i.strip() for i in skill]
        self.skillSet.extend([i.strip() for i in skill])

        print "self.designation-",self.designation
        print "self.skillSet-",self.skillSet



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

