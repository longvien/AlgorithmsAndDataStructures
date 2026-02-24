from BinaryNode import *
from BinarySearchTree import *
#basic tree
node1 = BinaryNode("root")
node2 = BinaryNode("left")
node3 = BinaryNode("right")
node1.left = node2
node1.right = node3


BST = BinarySearchTree()
# BST.addNode(10)
# BST.addNode(5)
# BST.addNode(8)
BST.root = BinaryNode(8)
BST.root.left = BinaryNode(3)
BST.root.left.left  = BinaryNode(1)
BST.root.left.right = BinaryNode(6)
BST.root.left.right.left = BinaryNode(4)
BST.root.left.right.right = BinaryNode(7)
BST.root.right = BinaryNode(10)
BST.root.right.right = BinaryNode(14)
BST.search(4)
# BST.preOrderTraversal(print) # current -> left -> right | Pre-order Traversal
# BST.inOrderTraversal(print) # left -> current -> right | In-order Traversal (Sorted)
# BST.postOrderTraversal(print) # left -> right -> current | Post-order Traversal (Sorted)
