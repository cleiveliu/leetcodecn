class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        ret = 0
        while i < j:
            ret = max(ret, min(nums[i], nums[j]) * (j - i))
            if nums[i] < nums[j]:
                i += 1
            else:
                j -= 1
        return ret
