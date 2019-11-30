# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ret = []
        stack = [root]
        reverse = False
        while stack:
            new_stack = []
            tem = []
            for node in stack:
                tem.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            if reverse:
                ret.append(tem[::-1])
            else:
                ret.append(tem)
            stack = new_stack
            reverse = not reverse
        return ret
