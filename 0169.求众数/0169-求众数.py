class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = [nums[0],1]
        for num in nums[1:]:
            if num == ret[0]:
                ret[1] += 1
            elif ret[1] > 0:
                ret[1] -= 1
            else:
                ret[0] = num
                ret[1] = 1
        return ret[0]