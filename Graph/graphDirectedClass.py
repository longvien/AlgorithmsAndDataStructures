class graphDirected:
    def __init__(self):
        self.adj = {}
        self.visited = []
    def addDirectedEdge(self, a, b):
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []
        self.adj[a].append(b)


    def DFSR(self):
        self.visited = []
        if self.adj:
            for i in self.adj:
                if i not in self.visited:
                    self._DFSR(i)
        return self.visited
    def _DFSR(self, n):
        pass