class Stack:
    def __init__(self):
        self.stack = []
    def push(self, node):
        self.stack.append(node)
    def pop(self):
        top = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]
        return top
    def isEmpty(self) -> bool:
        return len(self.stack) < 1
    def peek(self):
        return self.stack[len(self.stack) - 1]
