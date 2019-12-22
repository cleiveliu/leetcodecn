class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def h(s, n):
            return len(s) % n == 0 and h2(s, n)

        def h2(s, n):
            symbol = s[:n]
            return all(symbol == s[i : i + n] for i in range(0, len(s), n))

        return any(h(s, n) for n in range(1, len(s)))
