# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def postO(self, root):
        if root.left == None and root.right == None:
            self.count += 1
            return
        if root.left != None:
            self.postO(root.left)
        if root.right != None:
            self.postO(root.right)
        v1 = 0
        v2 = 0
        if root.left != None: v1 = root.left.val
        if root.right != None: v2 = root.right.val
        if root.val >= max(v1, v2):
            self.count += 1
        root.val = max(v1, v2, root.val)
    def countDominantNodes(self, root: Node | None) -> int:
        self.postO(root)
        return self.count