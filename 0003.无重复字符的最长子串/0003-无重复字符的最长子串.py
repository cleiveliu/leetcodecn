class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0
        i = 0
        d = {}
        for j in range(len(s)):
            if s[j] in d:
                i = max(i, d[s[j]] +1)
            ret = max(ret, j-i+1)
            d[s[j]] = j
        return ret