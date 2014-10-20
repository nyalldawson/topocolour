# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooser.ui'
#
# Created: Tue Oct 21 11:04:05 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(439, 408)
        self.vboxlayout = QtGui.QVBoxLayout(Dialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.layerFields = QtGui.QTreeWidget(Dialog)
        self.layerFields.setColumnCount(1)
        self.layerFields.setObjectName(_fromUtf8("layerFields"))
        self.vboxlayout.addWidget(self.layerFields)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.layerFields.headerItem().setText(0, QtGui.QApplication.translate("Dialog", "Select Layer and Field", None, QtGui.QApplication.UnicodeUTF8))

