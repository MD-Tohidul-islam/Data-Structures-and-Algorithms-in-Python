class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex, edge):
        self.gdict[vertex].append(edge)

customDict = {'a':['b','c'],
              'b':['a','d','e'],
              'd':['b','e','f'],
              'c':['a','e'],
              'e':['d','f','c'],
              'f':['d','e']}
graph = Graph(customDict)
print(graph.gdict)