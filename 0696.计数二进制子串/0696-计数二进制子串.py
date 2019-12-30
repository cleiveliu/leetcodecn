class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        
        count = 0 
        
        for i in range( len(s) -1 ):
            if (s[i] == '1' and s[i+1] == '0') or (s[i] == '0' and s[i+1] == '1'):
                ll = s[i]
                rr = s[i+1]
                l,r = i, i+1
                while l >= 0 and r < len(s) and s[l] == ll and s[r] == rr:
                    
                    count += 1
                    l -= 1
                    r += 1
        return count
                    