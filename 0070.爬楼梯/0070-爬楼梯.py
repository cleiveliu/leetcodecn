from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=128)
        def fib(n):
            if n <= 2:
                return n
            return fib(n - 1) + fib(n - 2)

        return fib(n)
