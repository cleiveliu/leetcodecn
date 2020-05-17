# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def h(root, sum_):
            if root == None:
                return 
            h(root.right, sum_)
            sum_[0] += root.val
            root.val = sum_[0]
            h(root.left, sum_)
        
        sum_ = [0]

        h(root, sum_)

        return root