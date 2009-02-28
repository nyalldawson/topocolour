
class Graph:
    def __init__(self,sorted=True):
        self.sorted = sorted
        self.nodeEdge = {}
        pass
    def addEdge(self,i,j):
        ij=[i,j]
        if self.sorted:
            ij.sort()
        (i,j)=ij
        if self.nodeEdge.has_key(i):
            self.nodeEdge[i].add(j)
        else:
            self.nodeEdge[i]=set([j])
    def dump(self):
        out = []
        for k in self.nodeEdge.keys():
            out.append( str(k)+":")
            for v in self.nodeEdge[k]:
                out.append(" --> "+str(v))
        return "\n".join(out)

    def writeDot(self,name,filePath):
        dot=self.makeDot(name)
        fp = file(filePath,"w")
        fp.write(dot)
        fp.close()

    def makeDot(self,name):
        s=[ 'graph "%s" {' % name ]
        for k in self.nodeEdge.keys():
            for v in self.nodeEdge[k]:
                s.append('"%s" -- "%s" ;' %(str(k),str(v)))
        s.append("}")
        return "\n".join(s)

    def makefull(self):
        g = Graph(sorted=False)
        for k in self.nodeEdge.keys():
            for v in self.nodeEdge[k]:
                g.addEdge(v,k)
                g.addEdge(k,v)
        return g
            

