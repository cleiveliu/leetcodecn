
from functools import lru_cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def square(x):
            return x*x
        @lru_cache(maxsize=32)
        def h(x,n):
            if n == 0:
                return 1
            if n & 1 == 0:
                return square( h(x,n//2) )
            else:
                return x * h(x, n-1)
        return h(x,n) if n > 0 else 1/h(x,-n)
            
        