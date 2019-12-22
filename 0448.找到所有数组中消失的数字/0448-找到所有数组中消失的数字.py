class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # return list(set((range(1,len(nums)+1))) - set(nums))
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -(abs(nums[index]))
        return [i + 1 for i, x in enumerate(nums) if x > 0]
