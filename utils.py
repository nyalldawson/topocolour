
from qgis.core import *
from qgis.gui import *

def polygonLayers(mapCanvas):
    layers = []
    for i in range(mapCanvas.layerCount()):
        layer = mapCanvas.layer(i)
        if layer.type() == layer.VectorLayer:
            if layer.geometryType() == QGis.Polygon:
                layers.append(layer)
    return layers

def fieldNames(layer):
    p = layer.dataProvider()
    fm = p.fields()
    names = []
    for f in fm:
        names.append(fm[f].name())
    # array of QStrings
    return names

