class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, path, ret, index):
            if index >= len(nums):
                ret.append(path)
                return
            helper(nums, path, ret, index + 1)
            helper(nums, path + [nums[index]], ret, index + 1)
            return ret

        ret = []
        helper(nums, [], ret, 0)
        return ret
