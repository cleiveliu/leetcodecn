# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def h(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            h(root.left)
            h(root.right)

        h(root)
        return root
