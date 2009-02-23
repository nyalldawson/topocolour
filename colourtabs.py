# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colourtabs.ui'
#
# Created: Mon Feb 23 18:39:44 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,418,478).size()).expandedTo(Dialog.minimumSizeHint()))

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

        self.layerCountLabel = QtGui.QLabel(self.colouringTab)
        self.layerCountLabel.setObjectName("layerCountLabel")
        self.vboxlayout1.addWidget(self.layerCountLabel)

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

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.saveDotFile = QtGui.QPushButton(self.colouringTab)
        self.saveDotFile.setObjectName("saveDotFile")
        self.hboxlayout1.addWidget(self.saveDotFile)
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
        self.vboxlayout1.addLayout(self.hboxlayout2)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)

        self.computeColouring = QtGui.QPushButton(self.colouringTab)
        self.computeColouring.setObjectName("computeColouring")
        self.hboxlayout3.addWidget(self.computeColouring)
        self.vboxlayout1.addLayout(self.hboxlayout3)

        spacerItem3 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem3)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem4)

        self.nowDoStyle = QtGui.QPushButton(self.colouringTab)
        self.nowDoStyle.setObjectName("nowDoStyle")
        self.hboxlayout4.addWidget(self.nowDoStyle)
        self.vboxlayout1.addLayout(self.hboxlayout4)
        self.processTabs.addTab(self.colouringTab,"")

        self.layerStyleTab = QtGui.QWidget()
        self.layerStyleTab.setEnabled(True)
        self.layerStyleTab.setObjectName("layerStyleTab")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.layerStyleTab)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.groupBox = QtGui.QGroupBox(self.layerStyleTab)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setContentsMargins(-1,9,-1,-1)
        self.gridlayout.setObjectName("gridlayout")

        self.dark2 = QtGui.QRadioButton(self.groupBox)
        self.dark2.setIcon(QtGui.QIcon(":/icons/icons/dark2.png"))
        self.dark2.setIconSize(QtCore.QSize(64,16))
        self.dark2.setObjectName("dark2")
        self.gridlayout.addWidget(self.dark2,3,0,1,1)

        self.set1 = QtGui.QRadioButton(self.groupBox)
        self.set1.setIcon(QtGui.QIcon(":/icons/icons/set1.png"))
        self.set1.setIconSize(QtCore.QSize(64,16))
        self.set1.setObjectName("set1")
        self.gridlayout.addWidget(self.set1,0,0,1,1)

        self.set2 = QtGui.QRadioButton(self.groupBox)
        self.set2.setIcon(QtGui.QIcon(":/icons/icons/set2.png"))
        self.set2.setIconSize(QtCore.QSize(64,16))
        self.set2.setObjectName("set2")
        self.gridlayout.addWidget(self.set2,1,0,1,1)

        self.set3 = QtGui.QRadioButton(self.groupBox)
        self.set3.setIcon(QtGui.QIcon(":/icons/icons/set3.png"))
        self.set3.setIconSize(QtCore.QSize(64,16))
        self.set3.setObjectName("set3")
        self.gridlayout.addWidget(self.set3,2,0,1,1)

        self.pastel1 = QtGui.QRadioButton(self.groupBox)
        self.pastel1.setIcon(QtGui.QIcon(":/icons/icons/pastel1.png"))
        self.pastel1.setIconSize(QtCore.QSize(64,16))
        self.pastel1.setObjectName("pastel1")
        self.gridlayout.addWidget(self.pastel1,0,1,1,1)

        self.pastel2 = QtGui.QRadioButton(self.groupBox)
        self.pastel2.setIcon(QtGui.QIcon(":/icons/icons/pastel2.png"))
        self.pastel2.setIconSize(QtCore.QSize(64,16))
        self.pastel2.setObjectName("pastel2")
        self.gridlayout.addWidget(self.pastel2,1,1,1,1)

        self.accent = QtGui.QRadioButton(self.groupBox)
        self.accent.setIcon(QtGui.QIcon(":/icons/icons/accents.png"))
        self.accent.setIconSize(QtCore.QSize(64,16))
        self.accent.setObjectName("accent")
        self.gridlayout.addWidget(self.accent,2,1,1,1)

        self.paired = QtGui.QRadioButton(self.groupBox)
        self.paired.setIcon(QtGui.QIcon(":/icons/icons/paired.png"))
        self.paired.setIconSize(QtCore.QSize(64,16))
        self.paired.setObjectName("paired")
        self.gridlayout.addWidget(self.paired,3,1,1,1)
        self.vboxlayout2.addWidget(self.groupBox)

        self.groupBox_2 = QtGui.QGroupBox(self.layerStyleTab)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.hboxlayout5.addWidget(self.label_5)

        self.lineType = QtGui.QComboBox(self.groupBox_2)
        self.lineType.setObjectName("lineType")
        self.hboxlayout5.addWidget(self.lineType)
        self.vboxlayout3.addLayout(self.hboxlayout5)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.hboxlayout6.addWidget(self.label_6)

        self.lineWidth = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.lineWidth.setObjectName("lineWidth")
        self.hboxlayout6.addWidget(self.lineWidth)
        self.vboxlayout3.addLayout(self.hboxlayout6)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.hboxlayout7.addWidget(self.label_7)

        self.lineColour = QtGui.QPushButton(self.groupBox_2)
        self.lineColour.setFlat(False)
        self.lineColour.setObjectName("lineColour")
        self.hboxlayout7.addWidget(self.lineColour)
        self.vboxlayout3.addLayout(self.hboxlayout7)
        self.vboxlayout2.addWidget(self.groupBox_2)

        spacerItem5 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem5)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setObjectName("hboxlayout8")

        spacerItem6 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem6)

        self.applyStyle = QtGui.QPushButton(self.layerStyleTab)
        self.applyStyle.setObjectName("applyStyle")
        self.hboxlayout8.addWidget(self.applyStyle)

        self.saveStyle = QtGui.QPushButton(self.layerStyleTab)
        self.saveStyle.setObjectName("saveStyle")
        self.hboxlayout8.addWidget(self.saveStyle)
        self.vboxlayout2.addLayout(self.hboxlayout8)

        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setObjectName("hboxlayout9")

        spacerItem7 = QtGui.QSpacerItem(40,14,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem7)

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
        self.vboxlayout2.addLayout(self.hboxlayout9)
        self.processTabs.addTab(self.layerStyleTab,"")
        self.vboxlayout.addWidget(self.processTabs)

        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.label_8.setBuddy(self.layerName)
        self.label_9.setBuddy(self.fieldName)
        self.label_3.setBuddy(self.algorithm)
        self.label_5.setBuddy(self.lineType)
        self.label_6.setBuddy(self.lineWidth)
        self.label_7.setBuddy(self.lineColour)

        self.retranslateUi(Dialog)
        self.processTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Dialog.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.layerCountLabel.setText(QtGui.QApplication.translate("Dialog", "How many colours needed.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Field", None, QtGui.QApplication.UnicodeUTF8))
        self.saveDotFile.setText(QtGui.QApplication.translate("Dialog", "Save DOT File", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Select Algorithm", None, QtGui.QApplication.UnicodeUTF8))
        self.computeColouring.setText(QtGui.QApplication.translate("Dialog", "Compute Colouring", None, QtGui.QApplication.UnicodeUTF8))
        self.nowDoStyle.setText(QtGui.QApplication.translate("Dialog", "Now colour the layer...", None, QtGui.QApplication.UnicodeUTF8))
        self.processTabs.setTabText(self.processTabs.indexOf(self.colouringTab), QtGui.QApplication.translate("Dialog", "Graph Colouring", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Palette", None, QtGui.QApplication.UnicodeUTF8))
        self.dark2.setText(QtGui.QApplication.translate("Dialog", "Dark2", None, QtGui.QApplication.UnicodeUTF8))
        self.set1.setText(QtGui.QApplication.translate("Dialog", "Set1", None, QtGui.QApplication.UnicodeUTF8))
        self.set2.setText(QtGui.QApplication.translate("Dialog", "Set2", None, QtGui.QApplication.UnicodeUTF8))
        self.set3.setText(QtGui.QApplication.translate("Dialog", "Set3", None, QtGui.QApplication.UnicodeUTF8))
        self.pastel1.setText(QtGui.QApplication.translate("Dialog", "Pastel1", None, QtGui.QApplication.UnicodeUTF8))
        self.pastel2.setText(QtGui.QApplication.translate("Dialog", "Pastel2", None, QtGui.QApplication.UnicodeUTF8))
        self.accent.setText(QtGui.QApplication.translate("Dialog", "Accent", None, QtGui.QApplication.UnicodeUTF8))
        self.paired.setText(QtGui.QApplication.translate("Dialog", "Paired", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Outline Style", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Line Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Colour", None, QtGui.QApplication.UnicodeUTF8))
        self.applyStyle.setText(QtGui.QApplication.translate("Dialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.saveStyle.setText(QtGui.QApplication.translate("Dialog", "Save Style", None, QtGui.QApplication.UnicodeUTF8))
        self.brewerInfo.setText(QtGui.QApplication.translate("Dialog", "palette © info", None, QtGui.QApplication.UnicodeUTF8))
        self.processTabs.setTabText(self.processTabs.indexOf(self.layerStyleTab), QtGui.QApplication.translate("Dialog", "Layer Style", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
