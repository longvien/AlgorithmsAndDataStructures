from queueNode import QueueNode

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        newNode = QueueNode(value)
        if self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def dequeue(self):
        if self.head is not None:
            current = self.head
            self.head = self.head.next
            current.next = None
        else:
            self.tail = None
            return None

    def peek(self):
        if self.head is None:
            return None
        return self.head.value