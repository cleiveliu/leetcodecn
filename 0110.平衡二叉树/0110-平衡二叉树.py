# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and \
                abs(self.depth(root.left)- self.depth(root.right)) < 2
    @lru_cache(maxsize = 128)
    def depth(self,node):
        if not node:
            return 0
        return 1 + max(self.depth(node.left), self.depth(node.right))
        