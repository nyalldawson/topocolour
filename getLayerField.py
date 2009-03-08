
from PyQt4.QtCore import *
from PyQt4.QtGui import *


from chooser import Ui_Dialog


LAYER = 1002
FIELD = 1003

class LayerItem(QTreeWidgetItem):
    def __init__(self,parent,layer):
        QTreeWidgetItem.__init__(self,parent,QStringList(layer.name()),LAYER)
        self.layer = layer

class FieldItem(QTreeWidgetItem):
    def __init__(self,parent,layer,fieldIndex,field):
        QTreeWidgetItem.__init__(self,parent,QStringList(field.name()),FIELD)
        self.layer = layer
        self.fieldIndex = fieldIndex
        self.field = field
    
class Chooser(QDialog, Ui_Dialog):
    def __init__(self, layers):
        QDialog.__init__(self)
        self.clicked = None
        self.setupUi(self)

        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        layerFieldsTree = self.layerFields

        self.items = []
        for layer in layers:
            item = LayerItem(None, layer)
            fields = layer.dataProvider().fields()
            for k,v in zip(fields.keys(),fields.values()):
                jtem = FieldItem(item, layer, k, v)
            self.items.append(item)
        layerFieldsTree.insertTopLevelItems(0, self.items);
        for item in self.items:
            layerFieldsTree.expandItem(item)
        QObject.connect(self.layerFields,SIGNAL("itemClicked(QTreeWidgetItem*, int)"),self.clickedItem)
        QObject.connect(self.layerFields,SIGNAL("itemDoubleClicked(QTreeWidgetItem*, int)"),self.clickedItemDouble)
 
    def clickedItem(self, item, column):
        if item.type() == FIELD:
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
        else:
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
            
        self.clicked=item

    def clickedItemDouble(self,item,column):
        if item.type() == FIELD:
            self.clicked = item
            self.accept()
        else:
            self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

import sys
def main():
    app = QApplication(sys.argv[1:])
    md = Chooser2()
    md.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
