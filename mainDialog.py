from qgis.core import *
from qgis.gui import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from colourtabs import Ui_Dialog

import topology
import adjlayer
import colouring

class Form(QDialog,Ui_Dialog):
    def __init__(self, iface, layer, fieldIndex, field):
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.layer = layer
        self.fieldIndex = fieldIndex
        self.layerName.setText(layer.name())
        self.fieldName.setText(field.name())
        self.saveDotFile.clicked.connect(self.doSaveDotFile)
        self.addAdjacency.clicked.connect(self.doAddAdjacency)
        self.computeColouring.clicked.connect(self.doComputeColouring)
        self.saveToFieldButton.clicked.connect(self.saveColours)
        self.populateFieldCombo()
        self.saveToFieldButton.setEnabled(False)
        for key,alg in colouring.algorithms.iteritems():
            self.algorithm.addItem(alg['name'],key)

    def exec_(self):
        self.topology,self.idGraph = topology.compute(self.layer, self.fieldIndex, True)
        if not self.topology:
            return None
        else:
            self.graphDump.setText(self.topology.dump())
            QDialog.exec_(self)

    def doSaveDotFile(self):
        f=QFileDialog.getSaveFileName(self,"Save DOT file","","DOT Files (*.dot)")
        if f:
            self.topology.writeDot(self.layer.name(),f)

    def doAddAdjacency(self):
        aLayer = adjlayer.make(self.layer,self.idGraph,self.fieldIndex)
        QgsMapLayerRegistry.instance().addMapLayer(aLayer)

    def doComputeColouring(self):
        key = str(self.algorithm.itemData(self.algorithm.currentIndex()))
        alg = colouring.algorithms[key]
        fnAlg = alg['code']
        self.gColouring = fnAlg(self.topology)
        self.maxColours = max(self.gColouring.values())
        self.layerCountLabel.setText(str(self.maxColours)+" colours needed")
        self.saveToFieldButton.setEnabled(True)
    
    def populateFieldCombo(self):
        self.destFieldComboBox.clear()
        for f in self.layer.pendingFields():
            self.destFieldComboBox.addItem( f.name() )
            
    def saveColours(self):
        destField = self.destFieldComboBox.currentText()
        destFieldIdx = self.destFieldComboBox.currentIndex()
        
        reply = QMessageBox.question(self, 'Save colours', "Are you sure you want to save colour numbers to the " + destField + " field?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No )
        if not reply == QMessageBox.Yes:
            return

        colorAttributes = {}
        for id, color in self.gColouring.iteritems():
            colorAttributes[id] = { destFieldIdx: color }
            
        self.layer.dataProvider().changeAttributeValues( colorAttributes )   
        
        self.layer.setCacheImage(None)
        self.iface.mapCanvas().refresh()
        QMessageBox.information(self, 'Save colours', "Colour numbers saved to " + destField + "!", QMessageBox.Ok )
