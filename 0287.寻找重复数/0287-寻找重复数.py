class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # I just can't
        return (sum(nums)-sum(set(nums)))//(len(nums)-len(set(nums)))
        