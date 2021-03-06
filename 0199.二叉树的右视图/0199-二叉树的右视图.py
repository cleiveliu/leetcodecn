# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        ret = []
        stack = [root]

        while stack:
            new_stack = []
            ret.append(stack[-1].val)
            while stack:
                node = stack.pop(0)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return ret
