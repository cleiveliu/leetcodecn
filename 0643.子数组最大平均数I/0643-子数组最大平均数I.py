class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k <= 0:
            return 0
        if k == 1:
            return max(nums) if nums else 0
        # k > 1; len(nums) >= k
        pre = nums[-1]
        nums[-1] = sum(nums[-k:])
        for i in range(len(nums)-2, k-2, -1):
            tem = nums[i]
            nums[i] = nums[i+1] - pre + nums[i-k+1]
            pre = tem
        return max(nums[k-1:])/k