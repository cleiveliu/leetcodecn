class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = dict()
        m[0] = 1
        ret = 0
        sum_ = 0
        for num in nums:
            sum_ += num
            if sum_ - k in m:
                ret += m[sum_ - k]
            m[sum_] = m.get(sum_, 0) + 1
        
        return ret