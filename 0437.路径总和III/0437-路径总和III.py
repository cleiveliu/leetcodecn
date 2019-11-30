# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, t: int) -> int:
        def h(node, cur, t, ret):
            if not node:
                return
            cur = cur + node.val
            if cur == t:
                ret.append(0)
            h2(node.left, 0, t, ret)
            h2(node.right, 0, t, ret)
            h(node.left, cur, t, ret)
            h(node.right, cur, t, ret)

        def h2(node, cur, t, ret):
            if not node:
                return
            cur = cur + node.val
            if cur == t:
                ret.append(0)
            h2(node.left, cur, t, ret)
            h2(node.right, cur, t, ret)

        ret = []
        h(root, 0, t, ret)

        return len(ret)
