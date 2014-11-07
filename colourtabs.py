# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colourtabs.ui'
#
# Created: Fri Nov 07 13:31:35 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(397, 333)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.hboxlayout.addWidget(self.label_8)
        self.layerName = QtGui.QLineEdit(Dialog)
        self.layerName.setReadOnly(True)
        self.layerName.setObjectName(_fromUtf8("layerName"))
        self.hboxlayout.addWidget(self.layerName)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.hboxlayout.addWidget(self.label_9)
        self.fieldName = QtGui.QLineEdit(Dialog)
        self.fieldName.setReadOnly(True)
        self.fieldName.setObjectName(_fromUtf8("fieldName"))
        self.hboxlayout.addWidget(self.fieldName)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.graphDump = QtGui.QTextEdit(self.groupBox)
        self.graphDump.setReadOnly(True)
        self.graphDump.setObjectName(_fromUtf8("graphDump"))
        self.vboxlayout.addWidget(self.graphDump)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.saveDotFile = QtGui.QPushButton(self.groupBox)
        self.saveDotFile.setObjectName(_fromUtf8("saveDotFile"))
        self.horizontalLayout.addWidget(self.saveDotFile)
        self.addAdjacency = QtGui.QPushButton(self.groupBox)
        self.addAdjacency.setObjectName(_fromUtf8("addAdjacency"))
        self.horizontalLayout.addWidget(self.addAdjacency)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.algorithm = QtGui.QComboBox(Dialog)
        self.algorithm.setObjectName(_fromUtf8("algorithm"))
        self.horizontalLayout_2.addWidget(self.algorithm)
        self.computeColouring = QtGui.QPushButton(Dialog)
        self.computeColouring.setObjectName(_fromUtf8("computeColouring"))
        self.horizontalLayout_2.addWidget(self.computeColouring)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layerCountLabel = QtGui.QLabel(Dialog)
        self.layerCountLabel.setText(_fromUtf8(""))
        self.layerCountLabel.setObjectName(_fromUtf8("layerCountLabel"))
        self.verticalLayout.addWidget(self.layerCountLabel)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.destFieldComboBox = QtGui.QComboBox(Dialog)
        self.destFieldComboBox.setObjectName(_fromUtf8("destFieldComboBox"))
        self.horizontalLayout_3.addWidget(self.destFieldComboBox)
        self.saveToFieldButton = QtGui.QPushButton(Dialog)
        self.saveToFieldButton.setObjectName(_fromUtf8("saveToFieldButton"))
        self.horizontalLayout_3.addWidget(self.saveToFieldButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_8.setBuddy(self.layerName)
        self.label_9.setBuddy(self.fieldName)
        self.label_3.setBuddy(self.algorithm)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.layerName, self.fieldName)
        Dialog.setTabOrder(self.fieldName, self.graphDump)
        Dialog.setTabOrder(self.graphDump, self.saveDotFile)
        Dialog.setTabOrder(self.saveDotFile, self.addAdjacency)
        Dialog.setTabOrder(self.addAdjacency, self.algorithm)
        Dialog.setTabOrder(self.algorithm, self.computeColouring)
        Dialog.setTabOrder(self.computeColouring, self.destFieldComboBox)
        Dialog.setTabOrder(self.destFieldComboBox, self.saveToFieldButton)
        Dialog.setTabOrder(self.saveToFieldButton, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_8.setText(_translate("Dialog", "Layer", None))
        self.label_9.setText(_translate("Dialog", "Field", None))
        self.groupBox.setTitle(_translate("Dialog", "Adjacencies", None))
        self.saveDotFile.setToolTip(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Save the adjacency graph as a DOT format file.</p></body></html>", None))
        self.saveDotFile.setText(_translate("Dialog", "Save DOT File", None))
        self.addAdjacency.setText(_translate("Dialog", "Add Adjacency Layer", None))
        self.label_3.setText(_translate("Dialog", "Colouring algorithm", None))
        self.computeColouring.setText(_translate("Dialog", "Compute Colouring", None))
        self.label.setText(_translate("Dialog", "Store color index in field", None))
        self.saveToFieldButton.setText(_translate("Dialog", "Save to Field", None))

import resources_rc
