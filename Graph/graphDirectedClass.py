from collections import deque
class directedGraph:
    def __init__(self):
        self.adj = {}
        self.visited = []
        self.visitedSet = set()
        self.queue = deque()
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
        self.visitedSet = set()
        if self.adj:
            for i in self.adj:
                if i not in self.visitedSet:
                    self._DFSR(i)
        return self.visited

    def _DFSR(self, node):
        if node not in self.visitedSet:
            self.visited.append(node)
            self.visitedSet.add(node)
            for n in self.adj[node]:
                if n not in self.visitedSet:
                    self._DFSR(n)
        return

    def DFS(self):
        self.visitedSet = set()
        self.visited = []
        self.stack = []
        for i in self.adj:
            if i not in self.visitedSet:
                self.visited.append(i)
                self.visitedSet.add(i)
                self.stack.append(i)
                while self.stack:
                    current = self.stack.pop()
                    for neighbor in self.adj[current]:
                        if neighbor not in self.visitedSet:
                            self.visited.append(neighbor)
                            self.visitedSet.add(neighbor)
                            self.stack.append(neighbor)
        return self.visited

    def BFS(self):
        self.visitedSet = set()
        self.visited = []
        self.queue = deque()
        for i in self.adj:
            if i not in self.visitedSet:
                self.visitedSet.add(i)
                self.visited.append(i)
                self.queue.append(i)
                while self.queue:
                    current = self.queue.popleft()
                    for n in self.adj[current]:
                        if n not in self.visitedSet:
                            self.visited.append(n)
                            self.visitedSet.add(n)
                            self.queue.append(n)
        return self.visited

    def cycleDetector(self):  # Idea: if neighbor in recStack, return Cycle Detected. Uses RecStack + Visited
        self.recStack = []
        self.visitedSet = set()
        self.visited = []
        self.cycleFound = False
        for i in self.adj:
            if self.cycleFound:
                break
            if i not in self.visitedSet:
                self._cycleDetector(i)
        return self.cycleFound

    def _cycleDetector(self, node):
        if self.cycleFound:
            return
        self.recStack.append(node)
        for neighbor in self.adj[node]:
            if neighbor not in self.visitedSet and neighbor not in self.recStack:
                self._cycleDetector(neighbor)
            elif neighbor in self.recStack:
                self.cycleFound = True
                return
        current = self.recStack.pop()
        self.visited.append(current)
        self.visitedSet.add(current)

    def topologicalSort(self):
        self.recStack = []
        self.topo = []
        if self.adj and self.cycleDetector() is False:
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
        if self.adj and self.cycleDetector() is False:
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