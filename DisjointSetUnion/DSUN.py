class DSUN:
    def __init__(self, n):
        self.parentA = [0 for i in range(n)]
    def makeSet(self, x):
        self.parentA[x] = x
    def find(self, x): # x = index, parent[x] = parent
        if x == self.parentA[x]:
            return x
        self.parentA[x] = self.find(self.parentA[x])
        return self.parentA[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parentA[rootX] = rootY
    def getWeight(self, edge):
        return edge[2]
    def KruskalAlgorithm(self, graph):
        edges = []
        mst = []
        for start, des, cost in graph:
            if self.parentA[start] != start:
                self.makeSet(start)
            if self.parentA[des] != des:
                self.makeSet(des)
            edges.append((start, des, cost))
        edges.sort(key=self.getWeight)
        for edge in edges:
            if self.find(edge[0]) != self.find(edge[1]):
                self.union(edge[0], edge[1])
                mst.append(edge)
        return mst