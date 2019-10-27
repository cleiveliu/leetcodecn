# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        def h(root, ret, path):
            if not root:
                return
            if not root.left and not root.right:
                path.append(root.val)
                ret.append('->'.join(map(str,path)))
                return
            h(root.left, ret, path +[root.val])
            h(root.right, ret, path +[root.val])
        ret = []
        h(root, ret, [])
        return ret