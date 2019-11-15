from collections import Counter
class Solution:
    def canConstruct(self, l: str, r: str) -> bool:
        l = Counter(l)
        r = Counter(r)
        
        return all(c in r and r[c] >= l[c] for c in l)