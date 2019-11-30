class Solution:
    def rob(self, nums: List[int]) -> int:
        ret = 0
        pre = 0
        for num in nums:
            temp = ret
            ret = max(ret, pre + num)
            pre = temp
        return ret
