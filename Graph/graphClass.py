class GraphClass:
    def __init__(self):
        self.adj = {}
    def addEdge(self, a, b):
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []
        self.adj[a].append(b)
        self.adj[b].append(a)
    def returnGraph(self):
        return self.adj
