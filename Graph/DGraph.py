from collections import deque
class DirectedGraph:
    def __init__(self):
        self.graph = {}
        self.visited = []
        self.visitedSet = set()
        self.stack = []
        self.queue = deque()
        self.recStack = []
        self.cycleFound = False
        self.topo = []
    def addEdges(self, a, b):
        if a not in self.graph:
            self.graph[a] = []
        if b not in self.graph:
            self.graph[b] = []
        self.graph[a].append(b)

    def DFSR(self):
        self.visitedSet = set()
        self.visited = []
        for i in self.graph:
            if i not in self.visitedSet:
                self._DFSR(i)
        return self.visited

    def _DFSR(self, node):
        if node not in self.visitedSet:
            self.visitedSet.add(node)
            self.visited.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in self.visitedSet:
                    self._DFSR(neighbor)

    def DFS(self):
        self.visited = []
        self.visitedSet = set()
        self.stack = []
        for i in self.graph:
            if i not in self.visitedSet:
                self.stack.append(i)
                while self.stack:
                    current = self.stack.pop()
                    self.visitedSet.add(current)
                    self.visited.append(current)
                    for neighbor in self.graph[current]: # reversed() | optional | so that order will be same as DFSR
                        if neighbor not in self.visitedSet and neighbor not in self.stack:
                            self.stack.append(neighbor)
        return self.visited

    def BFS(self):
        self.visited = []
        self.visitedSet = set()
        self.queue = deque()
        for i in self.graph:
            if i not in self.visitedSet:
                self.queue.append(i)
                while self.queue:
                    current = self.queue.popleft()
                    self.visited.append(current)
                    self.visitedSet.add(current)
                    for n in self.graph[current]:
                        if n not in self.visitedSet and n not in self.queue:
                            self.queue.append(n)
        return self.visited

    def componentsCounter(self):
        self.visitedSet = set()
        self.stack = []
        counter = 0
        for i in self.graph:
            if i not in self.visitedSet:
                counter += 1
                self.stack.append(i)
                while self.stack:
                    current = self.stack.pop()
                    self.visitedSet.add(current)
                    for n in self.graph[current]:
                        if n not in self.visitedSet and n not in self.stack:
                            self.stack.append(n)
        return counter

    def cycleDetector(self):
        self.visitedSet = set()
        self.cycleFound = False
        self.recStack = []
        for i in self.graph:
            if self.cycleFound:
                break
            if i not in self.visitedSet:
                self._cycleDetector(i)
        return self.cycleFound

    def _cycleDetector(self, node):
        self.recStack.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visitedSet and neighbor not in self.recStack:
                self._cycleDetector(neighbor)
            elif neighbor in self.recStack:
                self.cycleFound = True
                return
        if self.cycleFound:
            return
        current = self.recStack.pop()
        self.visitedSet.add(current)

    def topologicalSort(self):
        if not self.cycleDetector():
            self.topo = []
            self.visitedSet = set()
            self.recStack = []
            for i in self.graph:
                if i not in self.visitedSet:
                    self._topologicalSort(i)
            self.topo.reverse()
            return self.topo
        else:
            raise Exception("Graph is not a DAG. Topological Sort impossible!")

    def _topologicalSort(self, node):
        self.recStack.append(node)
        for neighbour in self.graph[node]:
            if neighbour not in self.visitedSet:
                self._topologicalSort(neighbour)
        current = self.recStack.pop()
        self.topo.append(current)
        self.visitedSet.add(current)

    def KahnAlgorithm(self):
        if not self.cycleDetector():
            self.queue = deque()
            indegree = {}
            self.topo = []
            for i in self.graph:
                if i not in indegree:
                    indegree[i] = 0
            for n in self.graph:
                for neighbour in self.graph[n]:
                    indegree[neighbour] += 1
            for nodes in indegree:
                if indegree[nodes] == 0:
                    self.queue.append(nodes)
            while self.queue:
                current = self.queue.popleft()
                self.topo.append(current)
                for a in self.graph[current]:
                    indegree[a] -= 1
                    if indegree[a] == 0:
                        self.queue.append(a)
            return self.topo
        else:
            raise Exception("Graph is not a DAG. Kahn's Algorithm impossible!")

