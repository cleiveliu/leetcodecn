class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        big1, big2 = 0,None
        for i in range(1,len(nums)):
            if nums[i] > nums[big1]:
                big1, big2 = i, big1
            elif big2 is None or nums[i] > nums[big2]:
                big2 = i
        return big1 if nums[big1] >= 2*nums[big2] else -1