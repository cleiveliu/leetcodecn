# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import functools


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def h(root):
            if not root:
                return
            l = calc(root.left)
            r = calc(root.right)
            h(root.left)
            h(root.right)
            ret.append(abs(l - r))

        @functools.lru_cache(None)
        def calc(node):
            if not node:
                return 0
            return node.val + calc(node.left) + calc(node.right)

        ret = []
        h(root)
        return sum(ret)
