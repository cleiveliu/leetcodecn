# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            new_stack =[]
            vals = []
            while stack:
                node = stack.pop(0)
                vals.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
            ret.append(vals)
        return list(map(lambda arr: sum(arr)/len(arr), ret))