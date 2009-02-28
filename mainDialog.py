from PyQt4.QtCore import *
from PyQt4.QtGui import *

from colourtabs import Ui_Dialog

import topology
import colouring

class Form(QDialog,Ui_Dialog):
    def __init__(self,layer,fieldIndex, field):
        QDialog.__init__(self)
        self.setupUi(self)
        self.layer = layer
        self.fieldIndex = fieldIndex
        self.layerName.setText(layer.name())
        self.fieldName.setText(field.name())
        QObject.connect(self.saveDotFile,SIGNAL("clicked()"),self.doSaveDotFile)
        QObject.connect(self.computeColouring,SIGNAL("clicked()"),self.doComputeColouring)
        self.processTabs.setTabEnabled(0,True)
        self.processTabs.setTabEnabled(1,False)
        self.nowDoStyle.setEnabled(False)
        self.processTabs.setCurrentIndex(0)
        for key,alg in colouring.algorithms.iteritems():
            self.algorithm.addItem(alg['name'],QVariant(key))

    def exec_(self):
        self.topology = topology.compute(self.layer, self.fieldIndex)
        if not self.topology:
            return None
        else:
            self.graphDump.setText(self.topology.dump())
            #self.topology = self.topology.makefull()
            QDialog.exec_(self)

    def doSaveDotFile(self):
        f=QFileDialog.getSaveFileName(self,"Save DOT file","","DOT Files (*.dot)")
        if f:
            self.topology.writeDot(self.layer.name(),f)


    def doComputeColouring(self):
        key = str(self.algorithm.itemData(self.algorithm.currentIndex()).toString())
        alg = colouring.algorithms[key]
        fnAlg = alg['code']
        self.gColouring = fnAlg(self.topology)
        self.maxColours = max(self.gColouring.values())
        self.layerCountLabel.setText(str(self.maxColours)+" colours needed")
        ok = True
        if ok:
            self.nowDoStyle.setEnabled(True)
            self.processTabs.setTabEnabled(1,True)
        

    def myfield(self):
        p = self.layer.dataProvider()
        name = p.fields()[self.fieldIndex].name()
        return name
