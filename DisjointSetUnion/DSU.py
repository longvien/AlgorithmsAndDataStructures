class DSU:
    def __init__(self):
        self.parent = {}
    def makeSet(self, x):
        self.parent[x] = x
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

    def getWeight(self, edge):
        return edge[2]

    def KruskalAlgorithm(self, graph):
        mst = []
        for start, des, cost in graph:
            if start not in self.parent:
                self.makeSet(start)
            if des not in self.parent:
                self.makeSet(des)
        edges = []
        for i in graph:
            edges.append(i)
        edges.sort(key=self.getWeight)
        for edge in edges:
            root0 = self.find(edge[0])
            root1 = self.find(edge[1])
            if root0 == root1:
                continue
            self.union(edge[0], edge[1])
            mst.append(edge)
        return mst





