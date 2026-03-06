from stackNode import StackNode

class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        newNode = StackNode(value)
        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
    def pop(self):
        if self.top is None:
            return None
        current = self.top
        self.top = current.next
        current.next = None
        return current
    def peek(self):
        if self.top is None:
            return None
        return self.top.value