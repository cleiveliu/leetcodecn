class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        break_point = [0]
        for i in range(len(s)+1):
            for j in break_point:
                if s[j:i] in wordDict:
                    break_point.append(i)
                    break
        return break_point[-1] == len(s)
        
        """
        def h(_set, s, i, j):
            if j >= len(s)-1 and s[i:j+1] in _set:
                return True
            else:
                return False
            if s[i:j+1] in _set:
                tmp = j
                return h(_set, s, tmp+1, j+1) or h(_set, s, i, j+1)
            else:
                return h(_set, s, i, j+1)
        _set = set(wordDict)
        return h(_set, s, 0, 0)
        """
            