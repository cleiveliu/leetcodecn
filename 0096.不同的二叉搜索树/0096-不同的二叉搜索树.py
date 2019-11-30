from functools import lru_cache


class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(maxsize=128)
        def h(left, right):
            if left >= right:
                return 1
            ret = 0
            for val in range(left, right + 1):
                left_diff = h(left, val - 1)
                right_diff = h(val + 1, right)
                ret += left_diff * right_diff
            return ret

        return h(1, n)
