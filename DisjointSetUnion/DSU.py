class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def makeSet(self, x):
        self.parent[x] = x
        self.size[x] = 1

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.size[rootX] > self.size[rootY]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        elif self.size[rootY] > self.size[rootX]:
            self.parent[rootX] = rootY #will be continue tomorrow (Tomorrow Start DP)

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



