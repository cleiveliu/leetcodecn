# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def h(node):
            ret = []
            if not node:
                return ret
            ret.extend(h(node.left))
            ret.append(node.val)
            ret.extend(h(node.right))
            return ret
        arr = h(root)
        if not arr:
            return True
        pre = arr[0]
        for a in arr[1:]:
            if a <= pre:
                return False
            pre = a
        return True
        