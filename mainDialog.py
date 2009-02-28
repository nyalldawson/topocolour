from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from colourtabs import Ui_Dialog

import topology
import colouring
import brewer

class Form(QDialog,Ui_Dialog):
    def __init__(self, iface, layer,fieldIndex, field):
        QDialog.__init__(self)
        self.setupUi(self)
        self.iface = iface
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

        # layer style tab setup
        QObject.connect(self.applyStyle,SIGNAL("clicked()"),self.doApplyStyle)
        # dont need this QObject.connect(self.saveStyle,SIGNAL("clicked()"),self.doSaveStyle)
        QObject.connect(self.brewerInfo,SIGNAL("clicked()"),self.doBrewerInfo)
        

    def exec_(self):
        self.topology = topology.compute(self.layer, self.fieldIndex)
        if not self.topology:
            return None
        else:
            self.graphDump.setText(self.topology.dump())
            QDialog.exec_(self)

    def doApplyStyle(self):
        print "apply style"
        name = str(self.colourScheme.currentText())
        print name,self.maxColours
        palette = brewer.palette(name,self.maxColours)
        #self.layer.symbols = [makeSymbol(self,rgb) for rgb in palette]
        self.layer.r = QgsUniqueValueRenderer(QGis.Polygon)
        self.layer.r.setClassificationField(self.fieldIndex)
        for k,v in self.gColouring.iteritems():
            #self.layer.r.insertValue(k,self.layer.symbols[v-1])
            self.layer.r.insertValue(k,makeSymbol(self,palette[v-1],k))
            
        self.layer.setRenderer(self.layer.r)
        self.iface.mapCanvas().refresh()
#    def doSaveStyle(self):
#        # TODO: save the qml here
#        print "save style"

    def doBrewerInfo(self):
        # TODO: write some doc here
        print "show brewer info"

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
            self.setupColourSchemes()
            self.nowDoStyle.setEnabled(True)
            self.processTabs.setTabEnabled(1,True)
    
    def setupColourSchemes(self):
        print "set the schemes combobox"
        self.colourScheme.setIconSize(QSize(64,16))
        for name,p in brewer.palettes.iteritems():
            if p['limits'][1] >= self.maxColours:
                self.colourScheme.addItem(QIcon(brewer.iconName(name)),name)
        # TODO: make sure we have at least one colour scheme

    def myfield(self):
        p = self.layer.dataProvider()
        name = p.fields()[self.fieldIndex].name()
        return name

def makeSymbol(self, rgb, v):
    s = QgsSymbol(QGis.Polygon,v,"","")
    s.setFillColor(QColor(rgb[0],rgb[1],rgb[2]))
    s.setFillStyle(Qt.SolidPattern)
    s.setColor(QColor(0,0,0))
    s.setLineWidth(0.5)
    return s
