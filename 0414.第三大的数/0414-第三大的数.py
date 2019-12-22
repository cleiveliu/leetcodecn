class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        one, two, three = [float("-inf")] * 3
        for num in set(nums):
            if num > one:
                one, two, three = num, one, two
            elif num > two:
                two, three = num, two
            elif num > three:
                three = num
        return three if three != float("-inf") else one
