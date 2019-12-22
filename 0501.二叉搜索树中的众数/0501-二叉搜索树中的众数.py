# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def to_arr(node):
            ret = []
            if node is None:
                return ret
            ret.extend(to_arr(node.left))
            ret.append(node.val)
            ret.extend(to_arr(node.right))
            return ret

        arr = to_arr(root)
        if len(arr) == 0:
            return []
        d = {}
        index = 0
        while index < len(arr):
            cur_val = arr[index]
            index += 1
            cnt = 1
            while index < len(arr) and arr[index] == cur_val:
                cnt += 1
                index += 1
            d[cur_val] = cnt
        max_cnt = max(d.values())

        return [k for k, v in d.items() if v >= max_cnt]
