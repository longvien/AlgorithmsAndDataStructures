from Stack import Stack
from Queue import Queue
from collections import deque
class GraphClass:
    def __init__(self):
        self.adj = {}
        self.visited = set() # O(1) check, output order randomly
        self.stack = Stack()
        self.queue = Queue()
        self.cycleFound = False
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
                if i not in self.visited:
                    self.cycleFound = False
                    self._DFSRecursive(i, None)
                if self.cycleFound:
                    print("Cycle")
        return self.visited

    def _DFSRecursive(self, node, parent):
        self.visited.add(node)
        for neighbor in self.adj[node]:
            if neighbor not in self.visited:
                self._DFSRecursive(neighbor, node)
            elif neighbor != parent:
                self.cycleFound = True
                return

    def DFSInterative(self):
        parent = None
        self.stack.stack = []
        self.visited = set()
        for i in self.adj:
            if i not in self.visited:
                self.stack.push(i)
                while not self.stack.isEmpty():
                    node = self.stack.pop()
                    self.visited.add(node)
                    parent = node
                    for current in self.adj[node]:
                        if current not in self.visited:
                            self.stack.push(current)
        return self.visited

    def BFS(self):
        self.queue.queue = []
        self.visited = set()
        for i in self.adj:
            if i not in self.visited:
                self.queue.enqueue(i)
                while not self.queue.isEmpty():
                    current = self.queue.dequeue()
                    self.visited.add(current)
                    for n in self.adj[current]:
                        if n not in self.visited:
                            self.queue.enqueue(n)
        return self.visited

    def componentsCounter(self) -> int:
        count = 0
        self.stack.stack = []
        self.visited = set()
        for i in self.adj:
            if i not in self.visited:
                count+=1
                self.stack.push(i)
                while not self.stack.isEmpty():
                    a = self.stack.pop()
                    self.visited.add(a)
                    for n in self.adj[a]:
                        if n not in self.visited:
                            self.stack.push(n)
        return count


