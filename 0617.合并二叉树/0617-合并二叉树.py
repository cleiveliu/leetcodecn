# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def h(n1, n2):
            if n1 and n2:
                n1.val += n2.val
                n1.left = h(n1.left, n2.left)
                n1.right = h(n1.right, n2.right)
                return n1
            else:
                return n1 or n2

        return h(t1, t2)
