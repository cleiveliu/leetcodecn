class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, nums, t, ret, cur, path):
            if cur == t:
                ret.append(path)
                return
            if cur > t or i >= len(nums):
                return
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[i]:
                j += 1
            helper(i + 1, nums, t, ret, cur + nums[i], path + [nums[i]])
            helper(j + 1, nums, t, ret, cur, path)

        nums.sort()
        ret = []
        helper(0, nums, target, ret, 0, [])
        return ret
