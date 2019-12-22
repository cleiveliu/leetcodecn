from functools import lru_cache


class Solution:
    def arrangeCoins(self, n: int) -> int:
        def x(n):
            return (1 + n) * n // 2

        if n == 0:
            return 0
        l, r = 1, n

        while l < r:
            mid = (l + r) // 2
            temp = x(mid)
            if temp > n and x(mid - 1) <= n:
                return mid - 1
            if temp <= n and x(mid + 1) > n:
                return mid

            if temp > n:
                r = mid
            elif n > temp:
                l = mid
            elif temp == n:
                return mid
        return l
