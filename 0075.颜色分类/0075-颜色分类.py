class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # they say use three pointer
        f, m = 0, 0
        l = len(nums) - 1
        while m <= l:
            if nums[m] == 2:
                nums[m], nums[l] = nums[l], nums[m]
                l -= 1
            elif nums[m] == 0:
                nums[m], nums[f] = nums[f], nums[m]
                if m > f:
                    nums[m] = 1
                m += 1
                f += 1
            elif nums[m] == 1:
                m += 1

        """
        record = {}
        
        for c in nums:
            record[c] = record.get(c, 0) + 1
        
        i = 0
        for n in range(3):
            times = record.get(n,0)
            for _ in range(times):
                nums[i] = n
                i += 1
        
        """
