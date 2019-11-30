# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def h(root):
            ret = []
            if not root:
                return ret
            ret.append(root.val)
            ret.extend(h(root.left))
            ret.extend(h(root.right))
            return ret

        return sum(filter(lambda x: L <= x <= R, h(root)))
