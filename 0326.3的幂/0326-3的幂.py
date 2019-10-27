class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def h(n):
            if n <= 0:
                return False
            if n == 1:
                return True
            if n%3 == 0:
                return h(n//3)
            return False
        return h(n)
        