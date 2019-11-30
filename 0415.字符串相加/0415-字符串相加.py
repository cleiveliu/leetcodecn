class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def calc(s1, s2, carry, ret):
            if not s1 and not s2 and carry == "0":
                return ret
            if not s1:
                return calc2(s2, carry, ret)
            if not s2:
                return calc2(s1, carry, ret)
            _, _, tem = h(s1[0], s2[0])
            n, carry, _ = h(tem, carry)
            ret.append(n)
            return calc(s1[1:], s2[1:], carry, ret)

        def calc2(s, carry, ret):
            if not s:
                if carry != "0":
                    ret.append(carry)
                return ret
            if carry == "0":
                for c in s:
                    ret.append(c)
                return ret
            n, carry, _ = h(s[0], carry)
            ret.append(n)
            return calc2(s[1:], carry, ret)

        def h(a, b):
            n = int(a) + int(b)
            return str(n % 10), str(n // 10), str(n)

        ret = calc(num1[::-1], num2[::-1], "0", [])

        return "".join(ret[::-1])
