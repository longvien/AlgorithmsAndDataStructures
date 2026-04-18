class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def makeSet(self, x):
        self.parent[x] = x
        self.size[x] = 1

    def find(self, x):
        if x in self.parent:
            if self.parent[x] == x:
                return x
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return False

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.size[rootX] > self.size[rootY]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        elif self.size[rootY] > self.size[rootX]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        return True

    def getWeight(self, edge):
        return edge[2]

    def Kruskal(self, graph, n):
        mst = []
        edges = list(graph)
        cost = 0
        count = 0
        for start, des, time in edges:
            if start not in self.parent:
                self.makeSet(start)
            if des not in self.parent:
                self.makeSet(des)
        edges.sort(key=self.getWeight)
        for edge in edges:
            if count == n-1:
                break
            if self.find(edge[0]) == self.find(edge[1]):
                continue
            self.union(edge[0], edge[1])
            cost += edge[2]
            mst.append(edge)
            count += 1
        return mst # or return cost, depends on task



