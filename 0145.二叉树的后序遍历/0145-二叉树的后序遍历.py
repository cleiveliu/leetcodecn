# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def post(node,ret):
            if node.left:
                post(node.left,ret)
            if node.right:
                post(node.right,ret)
            ret.append(node.val)
        if not root:
            return []
        
        ret = []
        post(root,ret)
        return ret
        