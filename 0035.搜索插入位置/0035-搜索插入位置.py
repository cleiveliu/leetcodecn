class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        else:
            return i + 1
