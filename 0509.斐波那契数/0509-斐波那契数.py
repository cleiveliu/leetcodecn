# from functools import wraps
class Solution:
    def fib(self, N: int) -> int:
        def simple_cache(fn):
            d = {}
            # @wraps
            def calc(n):
                if n in d:
                    return d[n]
                d[n] = fn(n)
                return d[n]
            return calc
        
        @simple_cache
        def fib(n):
            if n < 2:
                return n
            return fib(n-1) + fib(n-2)
        return fib(N)
        