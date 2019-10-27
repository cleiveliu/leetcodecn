# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def h(root):
            ret = [] 
            if not root:
                return ret
            ret.extend(h(root.left))
            ret.append(root.val)
            ret.extend(h(root.right))
            return ret
        arr = h(root)
        #print(arr)
        ret = float('inf')
        for i in range(len(arr)-1):
            ret = min(ret, arr[i+1]-arr[i])
        return ret