class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        cur = nums[0]
        slow, fast = 0, 0
        ret = float("inf")
        while (slow < len(nums) and fast < len(nums)) and ret != 1:
            if cur >= s:
                ret = min(ret, fast - slow + 1)
                cur -= nums[slow]
                slow += 1
            else:
                fast += 1
                if fast < len(nums):
                    cur += nums[fast]
        return ret if ret != float("inf") else 0
