# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root != None:
            if root.left == None:
                root = root.right
            else:
                left = root.left
                pre = left 
                while pre.right != None:
                    pre = pre.right
                pre.right = root.right
                root.right = left
                root.left = None

                root = root.right
            