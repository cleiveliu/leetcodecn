class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
            else:
                ret = max(ret, cur)
                cur = 0
        return max(ret, cur)