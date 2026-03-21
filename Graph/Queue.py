from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, node):
        self.queue.append(node)
    def dequeue(self):
        a = self.peek()
        self.queue.popleft()
        return a
    def peek(self):
        return self.queue[0]
    def isEmpty(self) -> bool:
        return len(self.queue) < 1