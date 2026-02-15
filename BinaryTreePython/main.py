from BinaryNode import *
from BinarySearchTree import *
#basic tree
node1 = BinaryNode("root")
node2 = BinaryNode("left")
node3 = BinaryNode("right")
node1.left = node2
node1.right = node3


BST = BinarySearchTree()
BST.addNode(5)
BST.root.left = BinaryNode(4)
BST.root.right = BinaryNode(6)
BST.preOrderTraversal(print) # current -> left -> right | Pre-order Traversal


