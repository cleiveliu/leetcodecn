class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a,2)+int(b,2))[2:]
        def bin2ten(s):
            ret = 0
            for i,c in enumerate(s[::-1]):
                if c == '1':
                    tem = 1 << i
                    ret += tem
            return ret
        def ten2bin(n):
            ret = ''
            while n > 0:
                ret += str(n%2)
                n //= 2
            if not ret:
                return '0'
            return ret[::-1]
        n1,n2 = bin2ten(a), bin2ten(b)
        ret = ten2bin(n1+n2)
        
        return ret