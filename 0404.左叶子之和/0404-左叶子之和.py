# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def h(node):
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + h(node.right)
            return h(node.left) + h(node.right)
        return h(root)
            