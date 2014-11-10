from qgis.core import *
from qgis.gui import *

import random
import operator
from collections import defaultdict

def randomGreedy(graph, debug=False):
    """ colour the nodes.... """
    colouring = {}
    colours = set()
    for k in graph.nodeEdge.keys():
        if debug:
            print "node *",k,"*"
        adjColours = set()
        for v in graph.nodeEdge[k]:
            if debug:
                print "nbor -- ",v
            if colouring.has_key(v):
                adjColours.add(colouring[v])
        if debug: 
            print "k's nbors are ",adjColours
        avail = colours.difference(adjColours)
        if debug:
            print "possible frees are ",avail
        if len(avail) == 0:
            # new colour
            newColour = len(colours)+1
            colours.add(newColour)
            if debug:
                print "new colour ",newColour," added."
        else:
            # use any free colour
            newColour = random.sample(avail,1)[0]
            if debug:
                print "using free colour ",newColour
        colouring[k]=newColour
    return colouring

def greedy(graph, debug=False):
    """ colour the nodes.... """
    colouring = {}
    colours = set()
    
    #calculate count of neighbours
    neighbourCount = {}
    QgsMessageLog.logMessage( str(graph.nodeEdge), 'Topocolor', QgsMessageLog.INFO )
    for k, v in graph.nodeEdge.iteritems():
        if neighbourCount.has_key(k):
            neighbourCount[k] += len(v)
        else:
            neighbourCount[k] = len(v)
            
    sortedByCount = sorted(neighbourCount.items(), key=operator.itemgetter(1), reverse=True)
    QgsMessageLog.logMessage( str(sortedByCount), 'Topocolor', QgsMessageLog.INFO )
    
    colourCounts = defaultdict(int)
    for ( k, c ) in sortedByCount:
        if debug:
            QgsMessageLog.logMessage( "node *" +str(k) + "*", 'Topocolor', QgsMessageLog.INFO )
        adjColours = set()
        for v in graph.nodeEdge[k]:
            if debug:
                QgsMessageLog.logMessage(  "nbor -- " + str(v), 'Topocolor', QgsMessageLog.INFO )
            if colouring.has_key(v):
                adjColours.add(colouring[v])
        if debug: 
            QgsMessageLog.logMessage(  "k's nbors are " + str(adjColours), 'Topocolor', QgsMessageLog.INFO )
        avail = colours.difference(adjColours)
        if debug:
            QgsMessageLog.logMessage(  "possible frees are " + str(avail), 'Topocolor', QgsMessageLog.INFO )
        if len(avail) == 0:
            #add new colour
            newColour = len(colours)+1
            colours.add(newColour)
            if debug:
                QgsMessageLog.logMessage(  "new colour " +str(newColour) +" added." , 'Topocolor', QgsMessageLog.INFO )
        else:
            # choose least used available colour
            counts = [ (c,v) for c,v in colourCounts.iteritems() if c in avail ]
            newColour = sorted(counts, key=operator.itemgetter(1) )[0][0]
            if debug:
                QgsMessageLog.logMessage(  "using free colour " + str(newColour), 'Topocolor', QgsMessageLog.INFO )
        colouring[k]=newColour
        colourCounts[newColour] += 1
    return colouring
    
algorithms = {'random': {'name': "Random", 'desc': 'Random Greedy Algorithm',
                         'code': randomGreedy},
              'greedy': {'name': "Greedy", 'desc': 'Greedy Algorithm',
                         'code': greedy},                         
              }

