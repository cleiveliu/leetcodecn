# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and \
                    is_mirror(n1.left, n2.right) and \
                    is_mirror(n1.right, n2.left)
        
        return is_mirror(root.left, root.right) if root else True
        
                    
        