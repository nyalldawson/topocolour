# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooser.ui'
#
# Created: Mon Feb 23 21:37:01 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,439,408).size()).expandedTo(Dialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Dialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.layerFields = QtGui.QTreeWidget(Dialog)
        self.layerFields.setColumnCount(1)
        self.layerFields.setObjectName("layerFields")
        self.vboxlayout.addWidget(self.layerFields)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Dialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Select Layer and field", None, QtGui.QApplication.UnicodeUTF8))
        self.layerFields.headerItem().setText(0,QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))

