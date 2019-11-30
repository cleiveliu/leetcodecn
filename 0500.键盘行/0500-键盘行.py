class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        ret = []
        for w in words:
            if any(s.issuperset(set(w.lower())) for s in (s1, s2, s3)):
                ret.append(w)
        return ret
