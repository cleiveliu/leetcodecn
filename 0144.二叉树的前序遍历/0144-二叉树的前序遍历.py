# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        ret = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ret
        """
        def helper(node,ret):
            if not node:
                return
            ret.append(node.val)
            helper(node.left,ret)
            helper(node.right,ret)
        
        ret = []
        helper(root,ret)
        
        return ret
        """