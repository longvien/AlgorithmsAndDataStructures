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

    def DijkstraAlgorithm(self, node):
        pq = []
        distance = {}
        self.visitedSet = set()
        parent = {}

        distance[node] = 0
        for i in self.graphD:
            if i not in distance:
                distance[i] = float("inf")
        heapq.heappush(pq, (distance[node], node))
        self.visitedSet.add(node)
        while pq:
            cost, node = heapq.heappop(pq)
            for neighbor in self.graphD[node]:
                if (cost + neighbor[1]) < distance[neighbor[0]]:
                    distance[neighbor[0]] = cost + neighbor[1]
                    parent[neighbor] = node
                    self.visitedSet.add(neighbor)
                    heapq.heappush(pq, (distance[neighbor[0]], neighbor[1]))
        for i in distance:
            print(f"{i} : {distance[i]}")


    # def DijkstraAlgorithm(self, sn, en):
    #     self.pq = []
    #     parent = {}
    #     self.visitedSet = set()
    #     distance = {sn: 0}
    #     for i in self.adjD:
    #         if i not in distance:
    #             distance[i] = float("inf")
    #         if i not in parent:
    #             parent[i] = None
    #         for a in self.adjD[i]:
    #             if a[1] not in distance:
    #                 distance[a[1]] = float("inf")
    #             if a[1] not in parent:
    #                 parent[a[1]] = None
    #     heapq.heappush(self.pq, (distance[sn], sn))
    #     while self.pq:
    #         priority, current = heapq.heappop(self.pq)
    #         if current not in self.visitedSet:
    #             self.visitedSet.add(current)
    #             for n in self.adjD[current]:
    #                 if (distance[current] + n[0]) < distance[n[1]]:
    #                     distance[n[1]] = distance[current] + n[0]
    #                     parent[n[1]] = current
    #                     heapq.heappush(self.pq, (distance[n[1]], n[1]))
    #         else:
    #             continue
    #     backtrack = []
    #     if distance[en] == float('inf'):
    #         print('Unreachable destination')
    #         return
    #     while en is not None:
    #         backtrack.append(en)
    #         en = parent[en]
    #     backtrack.reverse()
    #     return backtrack