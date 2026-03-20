from Stack import Stack
class GraphClass:
    def __init__(self):
        self.adj = {}
        self.tarray = []
    def addEdge(self, a, b):
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []
        self.adj[a].append(b)
        self.adj[b].append(a)

    def returnGraph(self):
        return self.adj

    def depthFirstSearch(self):
        for i in self.adj:
            self.tarray.append(i)
        self._depthFirstSearch(self.tarray[0], self.tarray)
    def _depthFirstSearch(self, n, array):
        stack = Stack()
        stack.push(n)
        stack.pop(n)
        for i in





