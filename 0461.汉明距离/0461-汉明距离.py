class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ret = 0
        num = x ^ y
        while num > 0:
            if num & 1 == 1:
                ret += 1
            num >>= 1
        return ret
