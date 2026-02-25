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

    # #addNode
    # def addNode(self, value : object):
    #     newNode = BinaryNode(value)
    #
    #     if self.root == None:
    #         self.root = newNode
    #         self.current = newNode
    #
    #     elif self.current.value > newNode.value:
    #         if self.current.left == None and newNode.value < self.current.value:
    #             self.current.left = newNode
    #             self.current = self.current.left
    #         else:
    #             while self.current.left is not None and newNode.value < self.current.value:
    #                 self.current = self.current.left
    #                 if self.current.value < newNode.value and self.current.right is not None and self.current.right.value < newNode.value:
    #                     self.current.right.right = newNode
    #                 elif self.current.value < newNode.value and self.current.right is not None and self.current.right.value > newNode.value:
    #                     self.current.right.left = newNode