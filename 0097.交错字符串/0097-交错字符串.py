from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        i,j,k = 0,0,0
        @lru_cache(None)
        def helper(i,j,k):
            if i == n1 and j == n2 and k == n3:
                return True
            elif i < n1 and j < n2 and s1[i] == s3[k] and s2[j] == s3[k]:
                return helper(i+1,j,k+1) or helper(i, j+1, k+1)
            elif i < n1 and s1[i] == s3[k]:
                return helper(i+1, j, k+1)
            elif j < n2 and s2[j] == s3[k]:
                return helper(i, j+1, k+1)
            else:
                return False
        return helper(0,0,0)
                
        