# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def cut(node):
            if node:
                if L <= node.val <= R:
                    node.left = cut(node.left)
                    node.right = cut(node.right)
                    
                    return node
                else:
                    left = cut(node.left)
                    right = cut(node.right)
                    
                    return left or right
        return cut(root)