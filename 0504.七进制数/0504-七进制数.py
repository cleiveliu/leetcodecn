class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        ret = ''
        neg = True if num < 0 else False
        num = abs(num)
        while num > 0:
            ret = str(num%7) + ret
            num = num//7
        return '-' + ret if neg else ret