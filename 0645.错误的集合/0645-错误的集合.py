class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ret = [0]*2
        nums.sort()
        cnt = 0
        for i in range(len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                if nums[i] == nums[i+1]:
                    ret[0] = nums[i]
                    cnt += 1
                    if cnt >= 2:
                        break
                if nums[i] + 2 == nums[i+1]:
                    ret[1] = nums[i]+1
                    cnt += 1
                    if cnt >= 2:
                        break
        if ret[1] == 0:
            if nums[0] != 1:
                ret[1] = 1
            else:
                ret[1] = len(nums)
        return ret