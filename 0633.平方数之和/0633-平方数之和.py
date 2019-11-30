class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
        l, r = 0, int(c ** 0.5) + 1
        while l <= r:
            val = l * l + r * r
            if val == c:
                return True
            elif val > c:
                r -= 1
            else:
                l += 1
        return False
