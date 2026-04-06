from collections import deque
class DirectedGraph:
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

    def addEdges(self, a, b):
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

    def topologicalSort(
            self):  # Idea: DFS until finish to recStack, pop from recStack, append to topo. After finish all: reversed(topo). Uses recStack + topo + visitedSet
        self.recStack = []
        self.topo = []
        if not self.cycleDetector():
            self.visitedSet = set()
            for i in self.adj:
                if i not in self.visitedSet:
                    self._topologicalSort(i)
            self.topo.reverse()
            return self.topo
        else:
            raise Exception("Graph is not a DAG, Cycle Detection Impossible!")

    def _topologicalSort(self, node):
        self.recStack.append(node)
        for neighbor in self.adj[node]:
            if neighbor not in self.visitedSet:
                self._topologicalSort(neighbor)
        current = self.recStack.pop()
        self.topo.append(current)
        self.visitedSet.add(current)

    def KahnAlgorithm(self): #Idea: 1st Create a indegree(incomingNodeNumber) dictionary. Always add all node with indegree = 0 to queue. Pop(), add node to topo reduce indegree of that node's neighbor. Continue until queue is empty. Uses: topo(final sorted), queue, visitedSet(markNodeAsVisited), indegreeDictionaries
        if not self.cycleDetector():
            self.topo = []
            indegree = {}
            self.queue = deque()
            self.visitedSet = set()
            for i in self.adj:
                if i not in indegree:
                    indegree[i] = 0
            for x in self.adj:
                for y in self.adj[x]:
                    indegree[y] += 1
            for n in self.adj:
                if indegree[n] == 0 and n not in self.visitedSet:
                    self.queue.append(n)
                    self.visitedSet.add(n)
            while self.queue:
                current = self.queue.popleft()
                self.topo.append(current)
                for i in self.adj[current]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        self.queue.append(i)
            return self.topo
        else:
            raise Exception("Graph is not a DAG, Cycle Detection Impossible!")