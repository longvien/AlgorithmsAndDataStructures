class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def binarySearch(self, val):
        self._binarySearch(val, self.root)
    def _binarySearch(self, val, node):
        if node is None:
            return None
        if val == node.val:
            return node
        elif val > node.val:
            self._binarySearch(val, node.left)
        elif val < node.val:
            self._binarySearch(val, node.right)