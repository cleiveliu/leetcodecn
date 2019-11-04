
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        l = nums.copy()
        pre = l[0]
        for i in range(1, len(l)):
            l[i] += pre
            pre = l[i]
        
        r = nums.copy()
        pre = r[-1]
        for i in range(len(r)-2,-1,-1):
            r[i] += pre
            pre = r[i]
        if len(r)>1 and r[1]==0:
            return 0
        
        for i in range(1,len(nums)-1):
            if l[i-1] == r[i+1]:
                return i
        if len(l) > 1 and l[-2] == 0:
            return len(nums)-1
        
        return -1