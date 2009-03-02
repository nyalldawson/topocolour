from qgis.core import *
from qgis.gui import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *


import showText

def show(s):
    window = QDialog()
    window.setModal(True)
    ui = showText.Ui_Dialog()
    ui.setupUi(window)
    ui.text.setText(s)
    window.show()
    window.exec_()
        
