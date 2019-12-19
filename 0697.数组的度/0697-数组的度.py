class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for i, val in enumerate(nums):
            if val in d:
                d[val][1] = i
                d[val][2] += 1
            else:
                d[val] = [i,i,1]
        ret = max(d.values(), key=lambda x:(x[2], -(x[1]-x[0])))
        
        return ret[1] - ret[0] + 1