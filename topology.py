

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *

from graph import Graph

def compute(layer, fieldNum, idGraph  = False):
    """ compute topology from a layer/field """

    f1 = QgsFeature()
    f2 = QgsFeature()

    s=Graph(sorted = False)
    if idGraph:
        ig = Graph(sorted=True)

    nFeatures = layer.featureCount()
    nops = ( nFeatures * (nFeatures-1) ) / 2.0

    progress = QProgressDialog("Computing topology...","Cancel", 0, nops)
    progress.setWindowModality(Qt.WindowModal)
    iop = 0

    fData = featureData(layer,fieldNum)

    for l1 in range(1,len(fData)):
        a1 = fData[l1]['att']
        g1 = fData[l1]['geom']

        for l2 in range(l1):
            progress.setValue(iop)
            if progress.wasCanceled():
                return None
            iop=iop+1
            g2 = fData[l2]['geom']
            if g1.intersects(g2):
                a2 = fData[l2]['att']
                s.addEdge(a1,a2)
                s.addEdge(a2,a1)
                if idGraph:
                    ig.addEdge(fData[l1]['id'],fData[l2]['id'])
    if not idGraph:
        return s
    else:
        return (s,ig)

def featureData(layer,fieldNum):
    fData = []
    p = layer.dataProvider()
    allAttrs = p.attributeIndexes()
    p.select(allAttrs)
    f = QgsFeature()
    while p.nextFeature(f):
        fData.append({
                'id': f.id(),
                'att': f.attributeMap()[fieldNum].toString(),
                'geom': f.geometryAndOwnership()
                })
    return fData
