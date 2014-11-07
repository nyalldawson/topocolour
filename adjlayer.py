from qgis.core import *
from qgis.gui import *
from PyQt4.QtGui import *

def make(layer,ig,attrNum):
    vl = QgsVectorLayer("LineString?crs=" + layer.crs().authid() + "&field=label:string&field=from:string&field=to:string&index=yes",layer.name()+"-adj.","memory")
    
    pr = vl.dataProvider()
    
    info = boxInfo(layer, attrNum)
    features = []
    for (f,tlist) in ig.nodeEdge.iteritems():
        for t in tlist:
            # make a feature from id=f to id=t
            centreF,labelF = info[f]
            ptF = QgsPoint(centreF[0],centreF[1])
            centreT,labelT = info[t]
            ptT = QgsPoint(centreT[0],centreT[1])

            feat = QgsFeature()
            feat.setGeometry(QgsGeometry.fromPolyline([ptF,ptT]))
            feat.setAttributes( [labelF+"-"+labelT, labelF, labelT] )
            features.append(feat)
            
    pr.addFeatures(features)
    return vl

def boxInfo(layer, fieldId):
    info = {}
    for f in layer.getFeatures():
        bbox = f.geometry().boundingBox()
        fString = str(f[fieldId])
        info[f.id()]= ((bbox.xMinimum() + bbox.width()/2.0, bbox.yMinimum() + bbox.height()/2.0), fString) 
        
    return info
        
        
