# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def h(root, t):
            if not root:
                return False
            if not root.left and not root.right and root.val == t:
                return True
            return h(root.left, t-root.val) or h(root.right, t-root.val)
        return h(root,sum)