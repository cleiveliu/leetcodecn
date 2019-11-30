import string


class Solution:
    def titleToNumber(self, s: str) -> int:
        upper_a = string.ascii_uppercase
        ret = 0
        for c in s:
            n = upper_a.index(c) + 1
            ret = ret * 26 + n
        return ret
