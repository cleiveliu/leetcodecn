# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def h(root):
            if not root:
                return 0
            return 1 + h(root.left) + h(root.right)
        return h(root)