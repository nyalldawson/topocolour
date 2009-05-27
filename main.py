#
# Rasterlang (c) Barry Rowlingson 2008
#
#    This file is part of "rasterlang"
#
#    Rasterlang is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Rasterlang is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Rasterlang.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import resources_rc
import getLayerField
import mainDialog
import utils

class MainPlugin(object):
  def __init__(self, iface):
    # Save a reference to the QGIS iface
    self.iface = iface

  def initGui(self):
    # Create action
    self.action = QAction(QIcon(":/icons/icons/topocolour.png"),"TopoColour",self.iface.mainWindow())
    self.action.setWhatsThis("Colour polygons by topology")
    QObject.connect(self.action,SIGNAL("activated()"),self.run)
    self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&TopoColour",self.action)

  def unload(self):
    # Remove the plugin
    self.iface.removePluginMenu("&TopoColour",self.action)
    self.iface.removeToolBarIcon(self.action)

  def run(self):
    """ do the whole thing """
    # choose a layer of polygons
    # choose an attribute
    # fire up the main dialog

    layers = utils.polygonLayers(self.iface.mapCanvas())
    chooser = getLayerField.Chooser(layers)
    status = chooser.exec_()
    if not status:
      return

    # compute topology

    main = mainDialog.Form(self.iface, chooser.clicked.layer, chooser.clicked.fieldIndex, chooser.clicked.field)
    main.exec_()
    
    pass

    
      
