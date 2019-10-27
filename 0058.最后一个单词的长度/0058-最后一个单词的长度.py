class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #return len(s.strip().split()[-1]) if s.strip().split() else 0
        ret = 0
        for c in s.strip()[::-1]:
            if c == ' ':
                return ret
            else:
                ret += 1
        return ret