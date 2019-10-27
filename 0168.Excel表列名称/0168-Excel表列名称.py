import string
class Solution:
    def convertToTitle(self, n: int) -> str:
        upper_a = string.ascii_uppercase
        ret = ''
        while n > 0:
            ret += upper_a[(n-1)%26]
            n = (n-1)//26
        return ret[::-1]