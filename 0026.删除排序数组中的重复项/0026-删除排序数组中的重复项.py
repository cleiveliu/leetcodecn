class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = 0
        for i, num in enumerate(nums):
            if num != nums[cur]:
                cur += 1
                nums[cur] = num
        return cur + 1
