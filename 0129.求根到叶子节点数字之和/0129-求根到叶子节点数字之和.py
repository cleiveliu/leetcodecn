# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def h(root, cur, ret):
            if not root:
                return
            if not root.left and not root.right:
                ret.append(cur * 10 + root.val)
                return
            if root.left:
                h(root.left, cur * 10 + root.val, ret)
            if root.right:
                h(root.right, cur * 10 + root.val, ret)

        ret = []
        h(root, 0, ret)

        return sum(ret)
