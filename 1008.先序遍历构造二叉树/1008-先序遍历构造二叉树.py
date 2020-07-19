# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def cut(xs, l, r, rootval):
            if l > r:
                return (None, None)
            if xs[l] > rootval:
                return (None, (l, r))
            if xs[r] < rootval:
                return ((l, r), None)
                
            mid = l
            while mid + 1 <= r and xs[mid+1] < rootval:
                mid += 1
            if mid >= r:
                return ((l, r), None)
            else:
                return ((l, mid), (mid+1, r))
        def build_by_preorder(xs, thisrange):
            if thisrange is None:
                return None
            l, r = thisrange
            root = TreeNode(xs[l])
            lrange, rrange = cut(xs, l+1, r, xs[l])
            root.left = build_by_preorder(xs, lrange)
            root.right = build_by_preorder(xs, rrange)

            return root
        
        if len(preorder) == 0:
            return None
        
        return build_by_preorder(preorder, (0, len(preorder)-1))
            