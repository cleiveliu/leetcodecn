class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = {str(x): x for x in range(10)}
        d2 = {x: str(x) for x in range(10)}

        def parse_num(s):
            ret = 0
            for c in s:
                n = d[c]
                ret = ret * 10 + n
            return ret

        def to_str(num):
            if num == 0:
                return "0"
            ret = ""
            while num:
                ret += d2[num % 10]
                num //= 10
            return ret[::-1]

        n1 = parse_num(num1)
        n2 = parse_num(num2)
        return to_str(n1 * n2)
