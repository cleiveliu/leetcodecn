# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def to_arr(node):
            ret = []
            if not node:
                return ret
            ret.extend(to_arr(node.left))
            ret.append(node.val)
            ret.extend(to_arr(node.right))

            return ret

        arr = to_arr(root)
        # print(arr)
        assert len(arr) >= 2, "yes it is"
        cur_min = float("inf")

        for i, num in enumerate(arr[1:]):
            cur_min = min(cur_min, abs(num - arr[i]))

        return cur_min
