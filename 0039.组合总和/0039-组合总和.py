class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        def helper(i,cur,path):
            if i >= n or cur > target:
                return
            if cur == target:
                ret.append(path)
                return
            helper(i,cur+nums[i],path+[nums[i]])
            helper(i+1,cur,path)
        ret = []
        n = len(nums)
        helper(0,0,[])
        return ret
        