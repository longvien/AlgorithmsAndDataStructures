class GraphClass:
    def __init__(self):
        self.adj = {}
        self.visited = []
        self.stack = []
        self.queue = []
        self.cycleDetected = False
    def addUndirectedEdge(self, a, b):
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []
        self.adj[a].append(b)
        self.adj[b].append(a)

    def returnGraph(self):
        return self.adj
    def DFSR(self):
        self.cycleDetected = False
        self.visited = []
        if self.adj:
            for i in self.adj:
                if i not in self.visited:
                    self._DFSR(i, None)
        return self.visited
    def _DFSR(self, n, parent):
        if self.cycleDetected:
            return
        if n in self.visited:
            return
        self.visited.append(n)
        for i in self.adj[n]:
            if self.cycleDetected:
                return
            if i not in self.visited:
                self._DFSR(i, n)
            elif i in self.visited and i != parent:
                print("Cycle")
                self.cycleDetected = True
                return

    def DFSI(self):
        self.cycleDetected = False
        self.visited = []
        self.stack = []
        if self.adj:
            for i in self.adj:
                if i not in self.visited:
                    self.stack.append((i, None))
                    while not self.isEmptyArr(self.stack):
                        a, parent = self.stack[len(self.stack) - 1]
                        del self.stack[len(self.stack) - 1]
                        self.visited.append(a)
                        for n in self.adj[a]:
                            if n not in self.visited and n not in [x[0] for x in self.stack]:
                                self.stack.append((n, a))
                            elif n in self.visited and n != parent and self.isEmptyArr(self.stack):
                                print("Cycle")
                                self.cycleDetected = True
                                return self.visited
        return self.visited

    def BFS(self):
        self.cycleDetected = False
        self.visited = []
        self.queue = []
        if self.adj:
            for i in self.adj:
                if i not in self.visited:
                    self.queue.append((i, None))
                    while not self.isEmptyArr(self.queue):
                        a, parent = self.queue[0]
                        del self.queue[0]
                        self.visited.append(a)
                        for n in self.adj[a]:
                            if n not in self.visited and n not in [e[0] for e in self.queue]:
                                self.queue.append((n, a))
                            elif n in self.visited and n != parent and self.isEmptyArr(self.queue):
                                print("Cycle")
                                self.cycleDetected = True
                                return self.visited
        return self.visited

    def isEmptyArr(self, arr) -> bool:
        return len(arr) < 1

    def componentsCounter(self) -> int:
        count = 0
        self.stack = []
        self.visited = []
        for i in self.adj:
            if i not in self.visited:
                count+=1
                self.stack.append(i)
                while not self.isEmptyArr(self.stack):
                    a = self.stack[len(self.stack) - 1]
                    del self.stack[len(self.stack) - 1]
                    self.visited.append(a)
                    for n in self.adj[a]:
                        if n not in self.visited:
                            self.stack.append(n)
        return count


