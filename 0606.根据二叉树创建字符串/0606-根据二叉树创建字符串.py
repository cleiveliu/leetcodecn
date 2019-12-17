# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def h(t):
            if not t:
                return ""
            if not t.left and not t.right:
                return str(t.val)
            if not t.left:
                return f"{str(t.val)}()({h(t.right)})"
            if not t.right:
                return f"{str(t.val)}({h(t.left)})"
            if t.left and t.right:
                return f"{str(t.val)}({h(t.left)})({h(t.right)})"
        return h(t)