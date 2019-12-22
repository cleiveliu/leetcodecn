class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        return sum(map(lambda x: x if x % 2 == 0 else x - 1, d.values())) + (
            1 if any(x % 2 == 1 for x in d.values()) else 0
        )
