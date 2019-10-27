class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        pre_min,pre_max = nums[0], nums[0]
        ret = nums[0]
        for num in nums[1:]:
            ret = max(pre_min*num, pre_max*num, ret, num)
            tmp = pre_max
            pre_max = max(pre_max*num, pre_min*num, num)
            pre_min = min(tmp*num, pre_min*num, num)
            print(pre_min,pre_max,ret)
        return ret