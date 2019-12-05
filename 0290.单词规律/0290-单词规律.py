class Solution:
    def wordPattern(self, p: str, strs: str) -> bool:
        strs = strs.split()
        if len(p) != len(strs):
            return False
        for (c1,c2) in zip(p,strs):
            if p.index(c1) != strs.index(c2):
                return False
        return True