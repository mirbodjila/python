# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fargo\OneDrive\Desktop\New folder\note.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys


class Ui_MainWindow(object):
    def __init__(self) -> None:
        super(Ui_MainWindow,self).__init__()
        loadUi("note.ui",self)
        self.actionnew.triggered.connect(self.new)
        self.actionopen.triggered.connect(self.open)
        self.actionsave.triggered.connect(self.save)
        self.actionsave_as.triggered.connect(self.saveas)
        self.actionundo.triggered.connect(self.undo)
        self.actioncut.triggered.connect(self.cut)
        self.actioncopy.triggered.connect(self.copy)
        self.actionpaste.triggered.connect(self.paste)
        self.actionword_wrap.triggered.connect(self.word_wrap)
        self.actionfont.triggered.connect(self.font)
    def newfile(self):
         
    def savefile(self):
       if self.current_path is not None:
           filetext=self.textedit.toPlaintext()
        else:
           self.savefileas 
    def openfile(self):
        fname=QFile        
            
    def savefileas(self)  :
        print("savefile As clicked")  
                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menuformat = QtWidgets.QMenu(self.menubar)
        self.menuformat.setObjectName("menuformat")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actionundo = QtWidgets.QAction(MainWindow)
        self.actionundo.setObjectName("actionundo")
        self.actioncut = QtWidgets.QAction(MainWindow)
        self.actioncut.setObjectName("actioncut")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.actionword_wrap = QtWidgets.QAction(MainWindow)
        self.actionword_wrap.setObjectName("actionword_wrap")
        self.actionfont = QtWidgets.QAction(MainWindow)
        self.actionfont.setObjectName("actionfont")
        self.actioncut_2 = QtWidgets.QAction(MainWindow)
        self.actioncut_2.setObjectName("actioncut_2")
        self.actioncopy_2 = QtWidgets.QAction(MainWindow)
        self.actioncopy_2.setObjectName("actioncopy_2")
        self.actionpaste = QtWidgets.QAction(MainWindow)
        self.actionpaste.setObjectName("actionpaste")
        self.menufile.addAction(self.actionnew)
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionsave)
        self.menufile.addAction(self.actionsave_as)
        self.menuedit.addAction(self.actionundo)
        self.menuedit.addAction(self.actioncut)
        self.menuedit.addAction(self.actioncopy)
        self.menuedit.addAction(self.actionpaste)
        self.menuformat.addAction(self.actionword_wrap)
        self.menuformat.addAction(self.actionfont)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menuformat.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.menuformat.setTitle(_translate("MainWindow", "format"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as"))
        self.actionundo.setText(_translate("MainWindow", "undo"))
        self.actioncut.setText(_translate("MainWindow", "cut"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))
        self.actionword_wrap.setText(_translate("MainWindow", "word wrap"))
        self.actionfont.setText(_translate("MainWindow", "font"))
        self.actioncut_2.setText(_translate("MainWindow", "cut"))
        self.actioncopy_2.setText(_translate("MainWindow", "copy"))
        self.actionpaste.setText(_translate("MainWindow", "paste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
