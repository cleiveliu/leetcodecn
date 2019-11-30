# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        stack = [root]
        while stack:
            new_stack = []
            for node in stack:
                if node.left and node.right:
                    new_stack.append(node.left)
                    new_stack.append(node.right)
                    if set([node.left.val, node.right.val]) == set([x, y]):
                        return False
                elif node.left:
                    new_stack.append(node.left)
                elif node.right:
                    new_stack.append(node.right)
            vals = [node.val for node in stack]
            if x in vals and y in vals:
                return True
            stack = new_stack
        return False
