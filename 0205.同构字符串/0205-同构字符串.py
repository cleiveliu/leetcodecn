class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return all(s.index(c1) == t.index(c2) for c1,c2 in zip(s,t)) if len(s) == len(t) else False