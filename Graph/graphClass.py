from Stack import Stack
from Queue import Queue
from collections import deque
class GraphClass:
    def __init__(self):
        self.adj = {}
        self.visited = set() # O(1) check, output order randomly
        self.stack = Stack()
        self.queue = Queue()
        #self.visited = [] O(n) check, inorder output

    def addEdge(self, a, b):
        if a not in self.adj:
            self.adj[a] = []
        if b not in self.adj:
            self.adj[b] = []
        self.adj[a].append(b)
        self.adj[b].append(a)
    def returnGraph(self):
        return self.adj

    def DFSRecursive(self):
        self.visited = set()
        if self.adj:
            for i in self.adj:
                self._DFSRecursive(i)
        return self.visited
    def _DFSRecursive(self, node):
        if node in self.visited:
            return
        self.visited.add(node)
        for i in self.adj[node]:
            self._DFSRecursive(i)

    def DFSInteractive(self):
        self.visited = set()
        self.stack.stack = []
        if self.adj:
            for node in self.adj:
                if node not in self.visited :
                    self.stack.push(node)
                    while not self.stack.isEmpty():
                        current = self.stack.pop()
                        self.visited.add(current)
                        for i in self.adj[current]:
                            if i not in self.visited:
                                self.stack.push(i)
        return self.visited

    def BFS(self):
        self.visited = set()
        self.queue.queue = deque()
        if self.adj:
            for i in self.adj:
                if i not in self.visited:
                    self.queue.enqueue(i)
                    while not self.queue.isEmpty():
                        current = self.queue.dequeue()
                        self.visited.add(current)
                        for items in self.adj[current]:
                            if items not in self.visited:
                                self.queue.enqueue(items)
        return self.visited





