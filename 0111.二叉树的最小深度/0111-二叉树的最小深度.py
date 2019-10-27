# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def h(root):
            if not root:
                return 0
            if root.left and root.right:
                return 1 + min(h(root.left), h(root.right))
            if not root.left and not root.right:
                return 1
            if root.left:
                return 1 + h(root.left)
            if root.right:
                return 1 + h(root.right)
        return h(root)