class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp
        return False
