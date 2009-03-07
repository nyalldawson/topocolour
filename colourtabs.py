# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colourtabs.ui'
#
# Created: Sat Mar  7 16:21:41 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,397,565).size()).expandedTo(Dialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Dialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.processTabs = QtGui.QTabWidget(Dialog)
        self.processTabs.setTabPosition(QtGui.QTabWidget.North)
        self.processTabs.setTabShape(QtGui.QTabWidget.Rounded)
        self.processTabs.setObjectName("processTabs")

        self.colouringTab = QtGui.QWidget()
        self.colouringTab.setEnabled(True)
        self.colouringTab.setObjectName("colouringTab")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.colouringTab)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.label_8 = QtGui.QLabel(self.colouringTab)
        self.label_8.setObjectName("label_8")
        self.hboxlayout.addWidget(self.label_8)

        self.layerName = QtGui.QLineEdit(self.colouringTab)
        self.layerName.setReadOnly(True)
        self.layerName.setObjectName("layerName")
        self.hboxlayout.addWidget(self.layerName)

        self.label_9 = QtGui.QLabel(self.colouringTab)
        self.label_9.setObjectName("label_9")
        self.hboxlayout.addWidget(self.label_9)

        self.fieldName = QtGui.QLineEdit(self.colouringTab)
        self.fieldName.setReadOnly(True)
        self.fieldName.setObjectName("fieldName")
        self.hboxlayout.addWidget(self.fieldName)
        self.vboxlayout1.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.saveDotFile = QtGui.QPushButton(self.colouringTab)
        self.saveDotFile.setObjectName("saveDotFile")
        self.hboxlayout1.addWidget(self.saveDotFile)

        self.addAdjacency = QtGui.QPushButton(self.colouringTab)
        self.addAdjacency.setObjectName("addAdjacency")
        self.hboxlayout1.addWidget(self.addAdjacency)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)

        self.label_3 = QtGui.QLabel(self.colouringTab)
        self.label_3.setObjectName("label_3")
        self.hboxlayout2.addWidget(self.label_3)

        self.algorithm = QtGui.QComboBox(self.colouringTab)
        self.algorithm.setObjectName("algorithm")
        self.hboxlayout2.addWidget(self.algorithm)

        self.computeColouring = QtGui.QPushButton(self.colouringTab)
        self.computeColouring.setObjectName("computeColouring")
        self.hboxlayout2.addWidget(self.computeColouring)
        self.vboxlayout1.addLayout(self.hboxlayout2)

        self.layerCountLabel = QtGui.QLabel(self.colouringTab)
        self.layerCountLabel.setObjectName("layerCountLabel")
        self.vboxlayout1.addWidget(self.layerCountLabel)

        self.groupBox = QtGui.QGroupBox(self.colouringTab)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.graphDump = QtGui.QTextEdit(self.groupBox)
        self.graphDump.setReadOnly(True)
        self.graphDump.setObjectName("graphDump")
        self.vboxlayout2.addWidget(self.graphDump)
        self.vboxlayout1.addWidget(self.groupBox)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)

        self.nowDoStyle = QtGui.QPushButton(self.colouringTab)
        self.nowDoStyle.setObjectName("nowDoStyle")
        self.hboxlayout3.addWidget(self.nowDoStyle)
        self.vboxlayout1.addLayout(self.hboxlayout3)
        self.processTabs.addTab(self.colouringTab,"")

        self.layerStyleTab = QtGui.QWidget()
        self.layerStyleTab.setEnabled(True)
        self.layerStyleTab.setObjectName("layerStyleTab")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.layerStyleTab)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.groupBox_2 = QtGui.QGroupBox(self.layerStyleTab)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.hboxlayout4.addWidget(self.label)

        self.colourScheme = QtGui.QComboBox(self.groupBox_2)
        self.colourScheme.setObjectName("colourScheme")
        self.hboxlayout4.addWidget(self.colourScheme)
        self.vboxlayout4.addLayout(self.hboxlayout4)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.hboxlayout5.addWidget(self.label_5)

        self.lineType = QtGui.QComboBox(self.groupBox_2)
        self.lineType.setObjectName("lineType")
        self.hboxlayout5.addWidget(self.lineType)
        self.vboxlayout4.addLayout(self.hboxlayout5)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.hboxlayout6.addWidget(self.label_6)

        self.lineWidth = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.lineWidth.setSingleStep(0.1)
        self.lineWidth.setProperty("value",QtCore.QVariant(0.5))
        self.lineWidth.setObjectName("lineWidth")
        self.hboxlayout6.addWidget(self.lineWidth)
        self.vboxlayout4.addLayout(self.hboxlayout6)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.hboxlayout7.addWidget(self.label_7)

        self.lineColour = QtGui.QPushButton(self.groupBox_2)
        self.lineColour.setFlat(False)
        self.lineColour.setObjectName("lineColour")
        self.hboxlayout7.addWidget(self.lineColour)
        self.vboxlayout4.addLayout(self.hboxlayout7)
        self.vboxlayout3.addWidget(self.groupBox_2)

        spacerItem3 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem3)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setObjectName("hboxlayout8")

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem4)

        self.applyStyle = QtGui.QPushButton(self.layerStyleTab)
        self.applyStyle.setObjectName("applyStyle")
        self.hboxlayout8.addWidget(self.applyStyle)
        self.vboxlayout3.addLayout(self.hboxlayout8)

        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setObjectName("hboxlayout9")

        spacerItem5 = QtGui.QSpacerItem(40,14,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem5)

        self.brewerInfo = QtGui.QPushButton(self.layerStyleTab)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brewerInfo.sizePolicy().hasHeightForWidth())
        self.brewerInfo.setSizePolicy(sizePolicy)
        self.brewerInfo.setMaximumSize(QtCore.QSize(16777215,17))

        font = QtGui.QFont()
        font.setPointSize(8)
        self.brewerInfo.setFont(font)
        self.brewerInfo.setObjectName("brewerInfo")
        self.hboxlayout9.addWidget(self.brewerInfo)
        self.vboxlayout3.addLayout(self.hboxlayout9)
        self.processTabs.addTab(self.layerStyleTab,"")
        self.vboxlayout.addWidget(self.processTabs)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.label_8.setBuddy(self.layerName)
        self.label_9.setBuddy(self.fieldName)
        self.label_3.setBuddy(self.algorithm)
        self.label.setBuddy(self.colourScheme)
        self.label_5.setBuddy(self.lineType)
        self.label_6.setBuddy(self.lineWidth)
        self.label_7.setBuddy(self.lineColour)

        self.retranslateUi(Dialog)
        self.processTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Dialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.processTabs,self.layerName)
        Dialog.setTabOrder(self.layerName,self.fieldName)
        Dialog.setTabOrder(self.fieldName,self.saveDotFile)
        Dialog.setTabOrder(self.saveDotFile,self.algorithm)
        Dialog.setTabOrder(self.algorithm,self.computeColouring)
        Dialog.setTabOrder(self.computeColouring,self.nowDoStyle)
        Dialog.setTabOrder(self.nowDoStyle,self.buttonBox)
        Dialog.setTabOrder(self.buttonBox,self.colourScheme)
        Dialog.setTabOrder(self.colourScheme,self.lineType)
        Dialog.setTabOrder(self.lineType,self.lineWidth)
        Dialog.setTabOrder(self.lineWidth,self.lineColour)
        Dialog.setTabOrder(self.lineColour,self.applyStyle)
        Dialog.setTabOrder(self.applyStyle,self.brewerInfo)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Field", None, QtGui.QApplication.UnicodeUTF8))
        self.saveDotFile.setToolTip(QtGui.QApplication.translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Save the adjacency graph as a DOT format file.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.saveDotFile.setText(QtGui.QApplication.translate("Dialog", "Save DOT File", None, QtGui.QApplication.UnicodeUTF8))
        self.addAdjacency.setText(QtGui.QApplication.translate("Dialog", "Add Adjacency Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Select Algorithm:", None, QtGui.QApplication.UnicodeUTF8))
        self.computeColouring.setText(QtGui.QApplication.translate("Dialog", "Compute Colouring", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Adjacencies", None, QtGui.QApplication.UnicodeUTF8))
        self.nowDoStyle.setText(QtGui.QApplication.translate("Dialog", "Now style the layer...", None, QtGui.QApplication.UnicodeUTF8))
        self.processTabs.setTabText(self.processTabs.indexOf(self.colouringTab), QtGui.QApplication.translate("Dialog", "Graph Colouring", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Colour Scheme", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Line Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Line Colour", None, QtGui.QApplication.UnicodeUTF8))
        self.applyStyle.setText(QtGui.QApplication.translate("Dialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.brewerInfo.setText(QtGui.QApplication.translate("Dialog", "palette © info", None, QtGui.QApplication.UnicodeUTF8))
        self.processTabs.setTabText(self.processTabs.indexOf(self.layerStyleTab), QtGui.QApplication.translate("Dialog", "Layer Style", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
