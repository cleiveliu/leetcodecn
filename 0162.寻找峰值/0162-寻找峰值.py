class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def h(arr, l, r):
            if l >= r:
                return l
            mid = (l + r) // 2
            if arr[mid] > arr[mid + 1]:
                return h(arr, l, mid)
            else:
                return h(arr, mid + 1, r)

        return h(nums, 0, len(nums) - 1)
