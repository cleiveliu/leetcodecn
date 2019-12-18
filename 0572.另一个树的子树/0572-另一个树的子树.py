# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def to_tuple(node):
            return (node.val, to_tuple(node.left), to_tuple(node.right)) if node else None
        return str(to_tuple(t)) in str(to_tuple(s))
        """
        def is_same(t1, t2):
            if t1 is None and t2 is None:
                return True
            if not (t1 and t2):
                return False
            return t1.val == t2.val and \
                    is_same(t1.left, t2.left) and \
                    is_same(t1.right, t2.right)
        
        def check(s, t):
            # t is not None
            if not s:
                return False
            if s.val == t.val:
                return is_same(s, t) or check(s.left, t) or check(s.right, t)
            else:
                return check(s.left, t) or check(s.right, t)
        
        if not t:
            return True
        
        return check(s, t)
        """