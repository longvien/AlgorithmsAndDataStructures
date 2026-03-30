class directedGraph:
    def __init__(self):
        self.adj = {}
        self.visited = []
        self.queue = []
        self.recStack = []
        self.stack = []
        self.topo = []
        self.indegree = {}
        self.cycleFound = False

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
        if n in self.visited:
            return
        self.visited.append(n)
        if self.adj[n]:
            for i in self.adj[n]:
                if i not in self.visited:
                    self._DFSR(i)

    def DFS(self):
        self.visited = []
        self.stack = []
        if self.adj:
            for i in self.adj:
                if i not in self.visited and i not in self.stack:
                    self.stack.append(i)
                while len(self.stack) > 0:
                    a = self.stack[len(self.stack) - 1]
                    del self.stack[len(self.stack) - 1]
                    self.visited.append(a)
                    for n in self.adj[a]:
                        if n not in self.visited and n not in self.stack:
                            self.stack.append(n)
        return self.visited

    def BFS(self):
        self.visited = []
        self.queue = []
        if self.adj:
            for i in self.adj:
                if i not in self.visited and i not in self.queue:
                    self.queue.append(i)
                    while len(self.queue) > 0:
                        a = self.queue[0]
                        del self.queue[0]
                        self.visited.append(a)
                        for n in self.adj[a]:
                            if n not in self.visited and n not in self.queue:
                                self.queue.append(n)
        return self.visited


    def CycleDetectionDFSI(self):
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

    def CycleDetectionDFSR(self) -> bool:
        self.visited = []
        self.recStack = []
        self.cycleFound = False
        if self.adj:
            for i in self.adj:
                if i not in self.visited and i not in self.recStack:
                    return self._CycleDetectionDFSR(i)
        return False

    def _CycleDetectionDFSR(self, n) -> bool:
        self.recStack.append(n)
        if self.adj[n]:
            for i in self.adj[n]:
                if i not in self.visited and i not in self.recStack:
                    return self._CycleDetectionDFSR(i)
                elif i in self.recStack:
                    self.cycleFound = True
                    return True
        self.recStack.remove(n)
        self.visited.append(n)
        return False

    def topologicalSort(self):
        self.recStack = []
        self.topo = []
        if self.adj and self.CycleDetectionDFSR() is False:
            self.recStack = []
            for i in self.adj:
                if i not in self.recStack and i not in self.topo:
                    self._topologicalSort(i)
            self.topo.reverse()
            return self.topo
        else:
            raise Exception("Cycle detected! Topological Sort impossible.")
    def _topologicalSort(self, node):
        self.recStack.append(node)
        for i in self.adj[node]:
            if i not in self.recStack and i not in self.topo:
                self._topologicalSort(i)
        self.topo.append(node)
        self.recStack.remove(node)

    def kahnAlgorithm(self):
        self.topo = []
        self.queue = []
        if self.adj and self.CycleDetectionDFSR() is False:
            for n in self.adj:
                self.indegree[n] = 0
            for i in self.adj:
                for neighbor in self.adj[i]:
                    self.indegree[neighbor] += 1
            for a in self.indegree:
                if self.indegree[a] == 0:
                    self.queue.append(a)
            while len(self.queue) > 0:
                b = self.queue.pop(0)
                self.topo.append(b)
                for d in self.adj[b]:
                    self.indegree[d] -= 1
                    if self.indegree[d] == 0:
                        self.queue.append(d)
            return self.topo
        else:
            raise Exception("Cycle detected! Kahn's Algorithm Sort Impossible")