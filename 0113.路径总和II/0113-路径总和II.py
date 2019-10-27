# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def h(root, path, ret, t):
            if not root:
                return
            if not root.left and not root.right and root.val == t:
                path.append(root.val)
                ret.append(path)
                return
            h(root.left, path +[root.val], ret, t-root.val)
            h(root.right, path+[root.val], ret, t-root.val)
        ret = []
        h(root, [], ret, sum)
        
        return ret