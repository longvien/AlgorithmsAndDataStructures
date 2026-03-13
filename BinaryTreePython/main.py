from BinaryNode import *
from BinarySearchTree import *
#basic tree
node1 = BinaryNode("root")
node2 = BinaryNode("left")
node3 = BinaryNode("right")
node1.left = node2
node1.right = node3

BST = BinarySearchTree()
BST.add(2)
BST.add(5)
BST.add(4)
BST.add(1)
BST.add(1.5)
BST.preOrderTraversal(print) # current -> left -> right | Pre-order Traversal
BST.inOrderTraversal(print) # left -> current -> right | In-order Traversal (Sorted)
BST.postOrderTraversal(print) # left -> right -> current | Post-order Traversal