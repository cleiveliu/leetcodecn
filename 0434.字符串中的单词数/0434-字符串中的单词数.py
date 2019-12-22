class Solution:
    def countSegments(self, s: str) -> int:
        index = 0
        ret = 0
        blank = " "
        while index < len(s) and s[index] == blank:
            index += 1
        while index < len(s):
            ret += 1
            while index < len(s) and s[index] != blank:
                index += 1
            while index < len(s) and s[index] == blank:
                index += 1
        return ret
