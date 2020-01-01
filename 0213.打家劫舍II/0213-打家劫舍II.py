class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        pre, now = 0, 0
        for num in nums[:-1]:
            pre, now = now, max(pre+num, now)
        ret = now
        pre, now = 0, 0
        for num in nums[1:]:
            pre, now = now, max(pre+num, now)
        
        ret = max(ret, now)
        
        return ret