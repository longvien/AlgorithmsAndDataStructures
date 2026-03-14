from BinaryNode import *
class BinarySearchTree:
    def __init__(self):
        self.root = None

    #preOrderTraversal
    def preOrderTraversal(self, action):
        self._preOrderTraversal(action, self.root)
    def _preOrderTraversal(self, action, node):
        if node != None:
            action(node.value)
            self._preOrderTraversal(action, node.left) # recursion
            self._preOrderTraversal(action, node.right) # recursion
    #inOrderTraversal
    def inOrderTraversal(self, action):
        self._inOrderTraversal(action, self.root)
    def _inOrderTraversal(self, action, node):
        if node is not None:
            self._inOrderTraversal(action, node.left)
            action(node.value)
            self._inOrderTraversal(action, node.right)

    #postOrderTraversal
    def postOrderTraversal(self, action):
        self._postOrderTraversal(action, self.root)
    def _postOrderTraversal(self, action, node):
        if node != None:
            self._postOrderTraversal(action, node.left)
            self._postOrderTraversal(action, node.right)
            action(node.value)

    #binarySearch
    def search(self, value):
        return self._search(self.root, value)
    def _search(self, node, value):
        if node is not None:
            print('Visiting: ', node.value)
        else:
            print("Value doesn't exist!")
            return None
        if node.value == value:
            return node
        if node.value > value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
    #addNode
    def add(self, value):
        if self.root is None:
            newNode = BinaryNode(value)
            self.root = newNode
            return
        self._add(value, self.root)
    def _add(self, value, node):
        if node.value < value and node.right is None:
            newNode = BinaryNode(value)
            node.right = newNode
            return
        elif node.value > value and node.left is None:
            newNode = BinaryNode(value)
            node.left = newNode
            return
        elif node.value > value:
            self._add(value, node.left)
        elif node.value < value:
            self._add(value, node.right)
    def getLeftMostNode(self, node):
        if node.left is None:
            return node
        self.getLeftMostNode(node.left)

    def remove(self, value):
        self._remove(self.root, value)
    def _remove(self, node, value):
        if self.root == value:
            self.root = self.getLeftMostNode(node.right)
        elif node.left.value == value:
            if node.left.left is None and node.left.right is None:
                node.left = None
            elif node.left.left is not None and node.left.right is None:
                node.left = node.left.left
            elif node.left.right is not None and node.left.left is None:
                node.left = node.left.right
            elif node.left.left is not None and node.left.right is not None:
                node.left = self.getLeftMostNode(node.left.right)
        elif node.right.value == value:
            if node.right.left is None and node.right.right is None:
                node.right = None
            elif node.right.right is not None and node.right.left is None:
                node.right = node.right.right
            elif node.right.left is not None and node.right.right is not None:
                node.right = self.getLeftMostNode(node.right.right)
        elif node.value < value:
            self._remove(node.right, value)
        elif node.value > value:
            self._remove(node.left, value)