import heapq
from collections import deque
class UndirectedGraph:
    def __init__(self):
        self.graph = {}
        self.graphD = { 'A': [('B', 4), ('C', 2)],
                        'B': [('A', 4), ('C', 5), ('D', 1)],
                        'C': [('A', 2), ('B', 5), ('D', 8), ('E', 3)],
                        'D': [('B', 1), ('C', 8), ('E', 6)],
                        'E': [('C', 3), ('D', 6)] }
        self.visitedSet = set()
        self.visited = []
        self.stack = []
        self.queue = deque()
        self.cycleFound = False
    def addEdges(self, a, b):
        if a not in self.graph:
            self.graph[a] = []
        if b not in self.graph:
            self.graph[b] = []
        self.graph[a].append(b)
        self.graph[b].append(a)

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
            for n in self.graph[node]:
                if n not in self.visitedSet:
                    self._DFSR(n)

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
                    for neighbor in self.graph[current]: # reversed() | optional |  so that order will be same as DFSR
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
                    self.visitedSet.add(current)
                    self.visited.append(current)
                    for neighbor in self.graph[current]:
                        if neighbor not in self.visitedSet and neighbor not in self.queue:
                            self.queue.append(neighbor)
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

    def cycleDetector(self) -> bool:
        self.cycleFound = False
        self.visitedSet = set()
        for i in self.graph:
            if self.cycleFound:
                break
            if i not in self.visitedSet:
                self._cycleDetector(i, None)
        return self.cycleFound

    def _cycleDetector(self, node, parent):
        self.visitedSet.add(node)
        for n in self.graph[node]:
            if self.cycleFound:
                return
            if n not in self.visitedSet:
                self._cycleDetector(n, node)
            elif n in self.visitedSet and n != parent:
                self.cycleFound = True
                return

    def DijkstraAlgorithm(self, node, destination):
        pq = [] # priority queue: Let's programme new what to process next
        distance = {} # distance: save distance from source node (node) to all other nodes
        parent = {} # parent: hold parent of each node for backtracking
        backtrack = [] # backtrack: saved backtracked node from destination to source

        # initialize src node
        distance[node] = 0
        parent[node] = None

        # set destination of other to infinity
        for i in self.graphD:
            if i not in distance:
                distance[i] = float("inf")
                parent[i] = None
        # push src node
        heapq.heappush(pq, (distance[node], node))
        while pq:
            cost, current = heapq.heappop(pq)
            if current == destination: # backtrack
                print(f"Length from {node} to {destination}: {distance[current]}")
                while current is not None:
                    backtrack.append(current)
                    current = parent[current]
                backtrack.reverse()
                return backtrack
            for n in self.graphD[current]: # loop neighbors and update if necessary
                if cost + n[1] < distance[n[0]]:
                    distance[n[0]] = cost + n[1]
                    heapq.heappush(pq, (distance[n[0]], n[0]))
                    parent[n[0]] = current
            else:
                continue
        raise Exception("Destination unreachable!!!")