class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        nums = set()
        n = 2
        start = 0
        while n ** start <= 10 ** 9:
            nums.add("".join(sorted(str(n ** start))))
            start += 1
        if "".join(sorted(str(N))) in nums:
            return True
        else:
            return False
