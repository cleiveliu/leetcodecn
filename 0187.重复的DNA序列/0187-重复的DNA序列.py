class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for i in range(0, len(s)-9):
            if s[i:i+10] in d:
                d[s[i:i+10]] = True
            else:
                d[s[i:i+10]] = False
        return list(k for k,v in d.items() if v == True)