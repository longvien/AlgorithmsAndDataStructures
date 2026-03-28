class graphDirected:
    def __init__(self):
        self.adj = {}
        self.visited = []
        self.recStack = []
        self.stack = []
        self.cycleFound = False
    def addDirectedEdge(self, a, b):
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []
        self.adj[a].append(b)

    def DFSR(self):
        self.visited = []
        self.recStack = []
        if self.adj:
            for i in self.adj:
                if i not in self.visited and  i not in self.recStack:
                    self._DFSR(i)
                if self.cycleFound:
                    while len(self.recStack) > 0:
                        a = self.recStack[len(self.recStack) - 1]
                        self.visited.append(a)
                        del self.recStack[len(self.recStack) - 1]
        return self.visited

    def _DFSR(self, n):
        self.recStack.append(n)
        if self.adj[n]:
            for i in self.adj[n]:
                if i not in self.visited and i not in self.recStack:
                    self._DFSR(i)
                elif i in self.recStack:
                    print("Cycle")
                    self.cycleFound = True
                    return
        else:
            while len(self.recStack) > 0:
                a = self.recStack[len(self.recStack) - 1]
                self.visited.append(a)
                del self.recStack[len(self.recStack) - 1]
            return


    def DFS(self):
        self.visited = []
        self.stack = []
        self.recStack = []
        self.cycleFound = False
        if self.adj:
            for i in self.adj:
                if i not in self.recStack and i not in self.visited:
                    self.stack.append(i)
                    while len(self.stack) > 0:
                        a = self.stack[len(self.stack) - 1]
                        del self.stack[len(self.stack) -1]
                        self.recStack.append(a)
                        if self.adj[a]:
                            for n in self.adj[a]:
                                if n not in self.recStack:
                                    self.stack.append(n)
                                else:
                                    print("Cycle")
                                    while len(self.recStack) > 0:
                                        b = self.recStack[len(self.recStack) - 1]
                                        del self.recStack[len(self.recStack) - 1]
                                        self.visited.append(b)
                        else:
                            while len(self.recStack) > 0:
                                b = self.recStack[len(self.recStack) - 1]
                                del self.recStack[len(self.recStack) - 1]
                                self.visited.append(b)
            return self.visited


