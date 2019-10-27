class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(l,r,n,ret,cur):
            if len(cur) > n*2:
                return
            if len(cur) == n*2 and l == r:
                ret.append(cur)
                return
            if l > r:
                helper(l+1,r,n,ret,cur+'(')
                helper(l,r+1,n,ret,cur+')')
            else:
                helper(l+1,r,n,ret,cur+'(')
        ret = []
        helper(0,0,n,ret,'')
        return ret
                