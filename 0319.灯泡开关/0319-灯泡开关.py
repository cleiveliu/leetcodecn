class Solution:
    def bulbSwitch(self, n: int) -> int:
        ret = 0
        for i in range(1,n+1):
            if i*i <= n:
                ret += 1
            else:
                break
        return ret