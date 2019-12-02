class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i < len(s) and j < len(t):
            while j < len(t) and t[j] != s[i]:
                j += 1
            while i < len(s) and j < len(t) and s[i] == t[j]:
                i += 1
                j += 1
        return i == len(s)