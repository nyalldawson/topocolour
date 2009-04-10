

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

    ids = featureIds(layer)

    for l1 in range(1,len(ids)):
        layer.featureAtId(ids[l1],f1)
        a1 = f1.attributeMap()[fieldNum].toString()
        g1 = f1.geometry()
        for l2 in range(l1):
            progress.setValue(iop)
            if progress.wasCanceled():
                return None
            iop=iop+1
            layer.featureAtId(ids[l2],f2)
            g2 = f2.geometry()
            if g1.intersects(g2):
                a2 = f2.attributeMap()[fieldNum].toString()
                s.addEdge(a1,a2)
                s.addEdge(a2,a1)
                if idGraph:
                    ig.addEdge(ids[l1],ids[l2])
    if not idGraph:
        return s
    else:
        return (s,ig)

def featureIds(layer):
    ids = []
    p = layer.dataProvider()
    allAttrs = p.attributeIndexes()
    p.select(allAttrs)
    f = QgsFeature()
    while p.nextFeature(f):        
        ids.append(f.id())
    return ids
