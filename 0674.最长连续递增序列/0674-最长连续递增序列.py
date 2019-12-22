class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ret = 0
        i = 0
        while i < len(nums):
            cur = 1
            while i + 1 < len(nums) and nums[i + 1] > nums[i]:
                cur += 1
                i += 1
            ret = max(ret, cur)
            i += 1
        return ret
