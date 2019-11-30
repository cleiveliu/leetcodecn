class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == t:
                return mid
            elif nums[mid] < nums[r]:
                # right is ordered
                if nums[mid] < t <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # left is ordered
                if nums[l] <= t < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
