class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[cur] = num
                cur += 1
        return cur
