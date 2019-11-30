# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def h(node):
            ret = []
            if not node:
                return ret

            if node.left:
                ret.extend(h(node.left))
            ret.append(node.val)
            if node.right:
                ret.extend(h(node.right))
            return ret

        return h(root)
