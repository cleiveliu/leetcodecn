# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def h(arr):
            if arr:
                mid = len(arr) // 2
                root = TreeNode(arr[mid])
                root.left = h(arr[:mid])
                root.right = h(arr[mid + 1 :])
                return root

        return h(nums)
