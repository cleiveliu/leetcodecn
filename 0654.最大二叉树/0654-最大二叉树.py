# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def build_tree(nums):
            if not nums:
                return None
            index, max_ = get_max(nums)
            root = TreeNode(max_)
            root.left = build_tree(nums[:index])
            root.right = build_tree(nums[index + 1 :])

            return root

        def get_max(nums):
            if not nums:
                return None, None
            index = 0
            ret = nums[0]
            for i, num in enumerate(nums):
                if num > ret:
                    ret = num
                    index = i
            return index, ret

        return build_tree(nums)
