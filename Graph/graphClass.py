from collections import deque
import heapq
class unDirectedGraph:
    def __init__(self):
        self.adj = {}
        self.adjD = {'A': [(3, 'C'), (2, 'F')],
                    'C': [(3, 'A'), (2, 'F'), (1, 'E')],
                    'E': [(1, 'C'), (2, 'B'), (3, 'F')],
                    'F': [(2, 'A'), (2, 'C'), (3, 'E'), (6, 'B'), (5, 'G')],
                    'D': [(4, 'C'), (1, 'B')],
                    'G': [(5, 'F'), (2, 'B')],
                    'B': [(1, 'D'), (2, 'E'), (2, 'G'), (6, 'F')],}
        self.visited = []
        self.visitedSet = set()
        self.stack = []
        self.pq = []
        self.queue = deque()
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
        self.visited = []
        self.visitedSet = set()
        if self.adj:
            for i in self.adj:
                if i not in self.visitedSet:
                    self._DFSR(i)
        return self.visited
    def _DFSR(self, n) -> None:
        if n in self.visitedSet:
            return
        self.visited.append(n)
        self.visitedSet.add(n)
        for i in self.adj[n]:
            if i not in self.visitedSet:
                self._DFSR(i)

    def DFS(self):
        self.visited = []
        self.stack = []
        self.visitedSet = set()
        if self.adj:
            for i in self.adj:
                if i not in self.visitedSet and i not in self.stack:
                    self.stack.append(i)
                while len(self.stack) > 0:
                    current = self.stack.pop()
                    self.visited.append(current)
                    self.visitedSet.add(current)
                    for n in self.adj[current]:
                        if n not in self.visitedSet and n not in self.stack:
                            self.stack.append(n)
        return self.visited

    def BFS(self):
        self.visited = []
        self.queue = deque()
        self.visitedSet = set()
        if self.adj:
            for i in self.adj:
                if i not in self.visitedSet and i not in self.queue:
                    self.queue.append(i)
                    while self.queue:
                        current = self.queue.popleft()
                        self.visited.append(current)
                        self.visitedSet.add(current)
                        for n in self.adj[current]:
                            if n not in self.visitedSet and n not in self.queue:
                                self.queue.append(n)
        return self.visited

    def CycleDetectionDFSR(self):
        self.cycleDetected = False
        self.visited = []
        if self.adj:
            for i in self.adj:
                if i not in self.visited:
                    self._CycleDetectionDFSR(i, None)
        return self.visited
    def _CycleDetectionDFSR(self, n, parent):
        if self.cycleDetected:
            return
        if n in self.visited:
            return
        self.visited.append(n)
        for i in self.adj[n]:
            if self.cycleDetected:
                return
            if i not in self.visited:
                self._CycleDetectionDFSR(i, n)
            elif i in self.visited and i != parent:
                print("Cycle")
                self.cycleDetected = True
                return

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

    def DijkstraAlgorithm(self, sn, en):
        self.pq = []
        parent = {}
        self.visitedSet = set()
        distance = {sn: 0}
        for i in self.adjD:
            if i not in distance:
                distance[i] = float("inf")
            if i not in parent:
                parent[i] = None
            for a in self.adjD[i]:
                if a[1] not in distance:
                    distance[a[1]] = float("inf")
                if a[1] not in parent:
                    parent[a[1]] = None
        heapq.heappush(self.pq, (distance[sn], sn))
        while self.pq:
            priority, current = heapq.heappop(self.pq)
            if current not in self.visitedSet:
                self.visitedSet.add(current)
                for n in self.adjD[current]:
                    if (distance[current] + n[0]) < distance[n[1]]:
                        distance[n[1]] = distance[current] + n[0]
                        parent[n[1]] = current
                        heapq.heappush(self.pq, (distance[n[1]], n[1]))
            else:
                continue
        backtrack = []
        if distance[en] == float('inf'):
            print('Unreachable destination')
            return
        while en is not None:
            backtrack.append(en)
            en = parent[en]
        backtrack.reverse()
        return backtrack

    # def CycleDetectionDFSI(self):
    #     self.cycleDetected = False
    #     self.visited = []
    #     self.stack = []
    #     if self.adj:
    #         for i in self.adj:
    #             if i not in self.visited:
    #                 self.stack.append((i, None))
    #                 while not self.isEmptyArr(self.stack):
    #                     a, parent = self.stack.pop()
    #                     self.visited.append(a)
    #                     for n in self.adj[a]:
    #                         if n not in self.visited and n not in [x[0] for x in self.stack]:
    #                             self.stack.append((n, a))
    #                         elif n in self.visited and n != parent:
    #                             print("Cycle")
    #                             self.cycleDetected = True
    #                             return self.visited
    #     return self.visited
    #
    # def cycleDetectionBFS(self):
    #     self.cycleDetected = False
    #     self.visited = []
    #     self.queue = []
    #     if self.adj:
    #         for i in self.adj:
    #             if i not in self.visited:
    #                 self.queue.append((i, None))
    #                 while not self.isEmptyArr(self.queue):
    #                     a, parent = self.queue[0]
    #                     del self.queue[0]
    #                     self.visited.append(a)
    #                     for n in self.adj[a]:
    #                         if n not in self.visited and n not in [e[0] for e in self.queue]:
    #                             self.queue.append((n, a))
    #                         elif n in self.visited and n != parent:
    #                             print("Cycle")
    #                             self.cycleDetected = True
    #                             return self.visited
    #     return self.visited