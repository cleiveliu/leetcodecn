class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
        ret = 0
        for key in d.keys():
            if key+1 in d:
                ret = max(ret, d[key]+ d[key+1])
        return ret