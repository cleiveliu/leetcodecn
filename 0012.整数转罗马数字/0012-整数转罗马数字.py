class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        chars = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        ret = ""
        i = 0
        while num > 0:
            if num >= vals[i]:
                ret += chars[i]
                num -= vals[i]
            else:
                i += 1
        return ret
