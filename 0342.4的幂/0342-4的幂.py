class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        def h(n):
            if n == 1:
                return True
            if n % 4 != 0 or n < 1:
                return False
            return h(n // 4)

        return h(num)
