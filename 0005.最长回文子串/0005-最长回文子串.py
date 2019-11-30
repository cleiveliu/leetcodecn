class Solution:
    def longestPalindrome(self, s: str) -> str:
        # noneffective

        def helper(s, n, i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1, j - i + 1

        ret = (0, 0, 0)
        n = len(s)
        for i in range(n):
            tem = helper(s, n, i, i)
            ret = tem if tem[2] > ret[2] else ret
            tem = helper(s, n, i, i + 1)
            ret = tem if tem[2] > ret[2] else ret
        i, j, _ = ret
        return s[i : j + 1]
