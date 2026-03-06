from collections.abc import Iterable
from Node.DoublyNode import DoublyNode


class DoublyLinkedList(Iterable):
    def __init__(self):
        self.head = None
        self.tail = None

    def reverseIterator(self):
        current = self.tail
        while current is not None:
            yield current.value # yield: return sth but won't exist the function. just pause it
            current = current.previous

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next


    def addHead(self, value):
        newNode = DoublyNode(value)
        if self.head is not None:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
        elif self.head is None and self.tail is None:
            self.head = newNode
            self.tail = newNode

    def addTail(self, value):
        newNode = DoublyNode(value)
        if self.tail is not None:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        elif self.tail is None and self.head is None:
            self.tail = newNode
            self.head = newNode

    def remove(self, value):
        node = self.head
        if self.contains(value):
            while node is not None:
                if node.value == value:
                    if self.head == self.tail:
                        self.head = None
                        self.tail = None
                    elif node.previous is None:
                        node.next.previous = None
                        self.head = node.next
                        node.next = None
                    elif node.next is None:
                        node.previous.next = None
                        self.tail = node.previous
                        node.previous = None
                    else:
                        node.previous.next = node.next
                        node.next.previous = node.previous
                        node.next = None
                        node.previous = None
                    break
                node = node.next
        else:
            raise Exception("Node doesn't exist")

    def removeHead(self):
        if self.head.next is not None:
            self.head.next.previous = None
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

    def removeTail(self):
        if self.tail.previous is not None:
            self.tail.previous.next = None
            self.tail = self.tail.previous
        else:
            self.head = None
            self.tail = None

    def returnValueHeadToTail(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def returnValueFromTailToHead(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.previous

    def find(self, value) -> DoublyNode:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def contains(self, value) -> bool:
        return self.find(value) is not None