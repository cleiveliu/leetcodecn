class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [(1,1)]*n 

        for i in range(n):
            for j in range(0,i+1):
                if nums[i] > nums[j]:
                    if dp[i][0] == dp[j][0] + 1:
                        val,count = dp[i]
                        _,count2 = dp[j]
                        dp[i] = (val, count+count2)
                    elif dp[i][0] < dp[j][0]+1:
                        val,count = dp[j]
                        dp[i] = (val+1, count)
        #print(dp)
        max_len = max(map(lambda x:x[0], dp))
        ret = sum(map(lambda x: x[1] if x[0] == max_len else 0, dp))

        return ret