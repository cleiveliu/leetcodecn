class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            nums[(num-1)%n] += n
        ret = []
        for i, num in enumerate(nums):
            if num > 2*n:
                ret.append(i+1)
        return ret
