class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def h(xs, start):
            # find the min x in xs[start+1:] that > xs[start] and swap them
            # where len(xs[start:]) >= 2
            pos = start + 1
            for i, x in enumerate(xs[start:], start=start):
                if x > xs[start] and x < xs[pos]:
                    pos = i
            xs[start], xs[pos] = xs[pos], xs[start]

        def h2(xs, start):
            # sort xs[start:] in place
            xs[start:] = sorted(xs[start:])

        flag = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                h(nums, i - 1)
                h2(nums, i)
                flag = True
                break
        if not flag:
            nums.sort()
