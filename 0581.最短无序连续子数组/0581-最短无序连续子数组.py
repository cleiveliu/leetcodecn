class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        ret = len(nums)
        i,j = 0, len(nums)-1
        
        while i < len(nums) and sort_nums[i] == nums[i]:
            i += 1
            ret -= 1
        
        while j >= i and sort_nums[j] == nums[j]:
            j -= 1
            ret -= 1
        
        return ret
            