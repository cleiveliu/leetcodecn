class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        if nums[-1] < 9:
            nums[-1] += 1
            return nums
        flag = 1
        nums[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            flag, nums[i] = (nums[i] + flag) // 10, (nums[i] + flag) % 10
            if not flag:
                break
        if flag:
            nums.insert(0, 1)
        return nums
