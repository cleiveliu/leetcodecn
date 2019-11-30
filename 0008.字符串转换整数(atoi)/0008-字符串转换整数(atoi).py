class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s or s[0].isalpha():
            return 0
        flag = -1 if s[0] == "-" else 1
        s = s[1:] if s[0] in ("+", "-") else s

        ret = 0
        for c in s:
            try:
                v = int(c)
                ret = ret * 10 + v
                if ret * flag > 2 ** 31 - 1:
                    return 2 ** 31 - 1
                elif ret * flag < -(2 ** 31):
                    return -(2 ** 31)
            except:
                return ret * flag
        return ret * flag
