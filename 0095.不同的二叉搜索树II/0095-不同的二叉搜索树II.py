# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def gen_trees(left, right):
            if left > right:
                return [None]

            all_trees = []
            for val in range(left, right + 1):
                left_trees = gen_trees(left, val - 1)
                right_trees = gen_trees(val + 1, right)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(val)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            return all_trees

        return gen_trees(1, n) if n >= 1 else []
