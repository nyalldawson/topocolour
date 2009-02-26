from PyQt4.QtCore import *
from PyQt4.QtGui import *

from colourtabs import Ui_Dialog

import topology

class Form(QDialog,Ui_Dialog):
    def __init__(self,layer,fieldIndex, field):
        QDialog.__init__(self)
        self.setupUi(self)
        self.layer = layer
        self.fieldIndex = fieldIndex
        self.layerName.setText(layer.name())
        self.fieldName.setText(field.name())
# prob need to put this somewhere else:
        self.topology = topology.compute(layer, fieldIndex)
        if not self.topology:
            self.reject()
# 

    def myfield(self):
        p = self.layer.dataProvider()
        name = p.fields()[self.fieldIndex].name()
        print name
        return name
        return p.fields()[self.fieldIndex]
