class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def h(s):
            if not s or len(s) == 1:
                return True
            return s[0] != s[1] and h(s[1:])

        return h(bin(n)[2:])
