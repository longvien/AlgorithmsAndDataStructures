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


