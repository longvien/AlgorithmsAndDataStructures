from BinaryNode import *
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.children = None
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


    def addNode(self, value):
        newNode = BinaryNode(value)
        if self.root == None:
            self.root = newNode
        elif newNode < self.root and self.children == None:
            self.root.left = newNode
            self.children  = newNode
        elif newNode >= self.root and self.children == None:
            self.root.right = newNode
            self.children = newNode
        elif newNode < self.root and self.children != None:
            if newNode < self.children:
                self.children.left = newNode
                self.children = newNode
            elif newNode >= self.children:
                self.children.right = newNode
                self.children = newNode




