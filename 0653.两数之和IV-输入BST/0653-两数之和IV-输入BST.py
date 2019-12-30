# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def gen(node):
            if node:
                yield from gen(node.left)
                yield node.val
                yield from gen(node.right)
        
        g = gen(root)
        
        s = set()
        
        for val in g:
            if val in s:
                return True
            s.add( k - val )
        
        return False