class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        x = abs(x)
        ret = 0
        while x > 0:
            ret = ret*10 + x%10
            x = x//10
        ret = -ret if neg else ret
        if ret < -2**31 or ret > 2**31 -1:
            return 0
        else:
            return ret