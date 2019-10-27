class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        xs = [False]*(n+1)
        for num in nums:
            if 0 < num < n + 1:
                xs[num] = True
        for i,x in enumerate(xs[1:], start=1):
            if not x:
                return i
        else:
            return n+1