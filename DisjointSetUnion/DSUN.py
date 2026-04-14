class DSUN:
    def __init__(self, x):
        self.parentArray = [i for i in range(x)] # array from 0 to x - 1
        self.size = [1 for i in range(x)] # array with x ones | [1] * x

    def find(self, x):
        if self.parentArray[x] == x:
            return x
        self.parentArray[x] = self.find(self.parentArray[x])
        return self.parentArray[x]

    def union(self, a, b) -> bool:
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False
        if self.size[rootA] > self.size[rootB]:
            self.parentArray[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        elif self.size[rootA] < self.size[rootB]:
            self.parentArray[rootA] = rootB
            self.size[rootB] += self.size[rootA]
        else:
            self.parentArray[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        return True

    def getWeight(self, edge):
        return edge[2]

    def Kruskal(self, graph, n):
        edges = list(graph)
        mst = []
        cost = 0
        count = 0
        edges.sort(key=self.getWeight)
        for edge in edges:
            if count == n - 1:
                break
            if self.find(edge[0]) == self.find(edge[1]):
                continue
            self.union(edge[0], edge[1])
            mst.append(edge)
            cost += edge[2]
            count += 1
        return cost









