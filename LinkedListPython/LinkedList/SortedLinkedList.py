from Node.SortedNode import sortedNode
class sortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        newNode = sortedNode(value)
        current = self.head
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif newNode.__lt__(self.head.value) <= 0:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
        elif newNode.__lt__(self.tail.value) >= 0:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            while newNode.__lt__(current.value) > 0:
                current = current.next
            current.previous.next = newNode
            newNode.previous = current.previous
            newNode.next = current
            current.previous = newNode

    def display(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
