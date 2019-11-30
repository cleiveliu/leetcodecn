class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = len(nums) - 1
        step = 0
        while index > 0:
            index -= 1
            step += 1
            if nums[index] >= step:
                step = 0
        return nums[index] >= step
