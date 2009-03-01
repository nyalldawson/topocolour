from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from colourtabs import Ui_Dialog

import topology
import colouring
import brewer
import display

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
        QObject.connect(self.nowDoStyle,SIGNAL("clicked()"),self.doNowDoStyle)
        self.processTabs.setCurrentIndex(0)
        for key,alg in colouring.algorithms.iteritems():
            self.algorithm.addItem(alg['name'],QVariant(key))

        # layer style tab setup
        QObject.connect(self.applyStyle,SIGNAL("clicked()"),self.doApplyStyle)
        QObject.connect(self.brewerInfo,SIGNAL("clicked()"),self.doBrewerInfo)

        # line styles
        self.lineType.addItem( QIcon( QgsSymbologyUtils.char2LinePixmap( "SolidLine" ) ), "Solid Line" , QVariant("SolidLine" ))
        self.lineType.addItem( QIcon( QgsSymbologyUtils.char2LinePixmap( "DashLine" ) ), "Dash Line" , QVariant("DashLine" ))
        self.lineType.addItem( QIcon( QgsSymbologyUtils.char2LinePixmap( "DotLine" ) ), "Dot Line" , QVariant("DotLine") )
        self.lineType.addItem( QIcon( QgsSymbologyUtils.char2LinePixmap( "DashDotLine" ) ),  "Dash Dot Line" , QVariant("DashDotLine") )
        self.lineType.addItem( QIcon( QgsSymbologyUtils.char2LinePixmap( "DashDotDotLine" ) ), "Dash Dot Dot Line" , QVariant("DashDotDotLine") )
        self.lineType.addItem( QIcon( QgsSymbologyUtils.char2LinePixmap( "NoPen" ) ), "No Pen" , QVariant("NoPen") )
        
        # line colour dialog
        QObject.connect(self.lineColour,SIGNAL("clicked()"),self.doLineColour)
        self.setLineColourButton(QColor(0,0,0))

    def exec_(self):
        self.topology = topology.compute(self.layer, self.fieldIndex)
        if not self.topology:
            return None
        else:
            self.graphDump.setText(self.topology.dump())
            QDialog.exec_(self)

    def doApplyStyle(self):
        name = str(self.colourScheme.currentText())
        palette = brewer.palette(name,self.maxColours)
        self.layer.r = QgsUniqueValueRenderer(QGis.Polygon)
        self.layer.r.setClassificationField(self.fieldIndex)
        for k,v in self.gColouring.iteritems():
            self.layer.r.insertValue(k,makeSymbol(self,palette[v-1],k))
            
        self.layer.setRenderer(self.layer.r)
        # redraw the map and refresh the legend
        self.iface.mapCanvas().refresh()
        self.iface.refreshLegend(self.layer)
        QgsProject.instance().dirty(True)

    def doBrewerInfo(self):
        display.show(brewer.doc)

    def doSaveDotFile(self):
        f=QFileDialog.getSaveFileName(self,"Save DOT file","","DOT Files (*.dot)")
        if f:
            self.topology.writeDot(self.layer.name(),f)

    def doNowDoStyle(self):
        self.processTabs.setCurrentIndex(1)

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


    def doLineColour(self):
        get = QColorDialog.getColor(QColor(255,255,255),self.iface.mapCanvas())
        if get:
            self.setLineColourButton(get)

    def setLineColourButton(self,colour):
        self.myLineColour = colour
        self.lineColour.setStyleSheet(
            "QPushButton { background-color: %s }"
            "QPushButton:pressed { background-color: %s}" % (colour.name(),colour.light(125).name())
            )


    def setupColourSchemes(self):
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
    s.setColor(self.myLineColour)
    #s.setColor(QColor(0,0,0))

    myLineStyle = self.lineType.itemData( self.lineType.currentIndex(), Qt.UserRole ).toString()
    s.setLineStyle( QgsSymbologyUtils.qString2PenStyle( myLineStyle ) )

    s.setLineWidth(self.lineWidth.value())

    return s
