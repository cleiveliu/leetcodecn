class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for any possible max subsets: part1: arr[:-1] partt2: arr[-1]
        # max(part1 + part2) = part1 + part2 if part1 > 0 else part2
        #
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)
