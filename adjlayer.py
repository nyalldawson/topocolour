
from PyQt4.QtCore import QVariant

from qgis.core import *
from qgis.gui import *

def make(layer,ig,attrNum):
    vl = QgsVectorLayer("LineString",layer.name()+"-adj.","memory")
    pr = vl.dataProvider()
    pr.addAttributes({"label":"string"})
    
    info = boxInfo(layer, attrNum)

    fet = QgsFeature()
    for (f,tlist) in ig.nodeEdge.iteritems():
        for t in tlist:
            # make a feature from id=f to id=t
            centreF,labelF = info[f]
            ptF = QgsPoint(centreF[0],centreF[1])
            centreT,labelT = info[t]
            ptT = QgsPoint(centreT[0],centreT[1])

            fet.setGeometry(QgsGeometry.fromPolyline([ptF,ptT]))
            fet.addAttribute(0,QVariant(labelF+"-"+labelT))
            pr.addFeatures([fet])
    vl.updateExtents()
    return vl
                            
    

def boxInfo(layer, fieldId):
    provider = layer.dataProvider()
    provider.rewind()
    provider.select([fieldId])
    f = QgsFeature()
    info = {}
    while provider.nextFeature(f):
        bbox = f.geometry().boundingBox()
        fString = f.attributeMap()[fieldId].toString()
        info[f.id()]= ((bbox.xMinimum() + bbox.width()/2.0, bbox.yMinimum() + bbox.height()/2.0), fString) 

    return info
        
        
