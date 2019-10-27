class Solution:
    def addDigits(self, n: int) -> int:
        if n < 10:
            return n
        return self.addDigits(n%10 + self.addDigits(n//10))