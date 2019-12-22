# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ret = [float("inf")] * 2

        def h(node):
            if node:
                if node.val < ret[-1]:
                    ret[-1], ret[0] = node.val, ret[-1]
                elif ret[-1] < node.val < ret[0]:
                    ret[0] = node.val

                h(node.left)
                h(node.right)

        h(root)
        return ret[0] if ret[0] != float("inf") else -1
