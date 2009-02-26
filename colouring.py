
import random

def greedy(graph, debug=False):
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

algorithms = {'greedy': {'name': "Greedy", 'desc': 'Random Greedy Algorithm',
                         'code': greedy},
              }

