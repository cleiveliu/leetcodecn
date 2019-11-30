class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1, -1]
        if not nums:
            return ret

        def findl(arr, l, r, t):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == t:
                    return (
                        mid
                        if findl(nums, l, mid - 1, t) is None
                        else findl(nums, l, mid - 1, t)
                    )
                elif nums[mid] > t:
                    r = mid - 1
                else:
                    l = mid + 1

        def findr(arr, l, r, t):
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == t:
                    return (
                        mid
                        if findr(nums, mid + 1, r, t) is None
                        else findr(nums, mid + 1, r, t)
                    )
                elif nums[mid] > t:
                    r = mid - 1
                else:
                    l = mid + 1

        l, r = 0, len(nums) - 1
        ret[0] = findl(nums, l, r, target)
        ret[1] = findr(nums, l, r, target)

        if ret[0] is None or ret[1] is None:
            return [-1, -1]
        return ret
