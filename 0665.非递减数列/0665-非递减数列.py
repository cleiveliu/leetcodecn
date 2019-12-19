class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums = [float('-inf')] + nums + [float('inf')]
        i = 1
        count = 0
        while i < len(nums) - 2:
            if nums[i] > nums[i+1]:
                count += 1
                if not (nums[i+1] >= nums[i-1] or nums[i+2] >= nums[i]):
                    return False
                if count > 1:
                    return False
            i += 1
        return True