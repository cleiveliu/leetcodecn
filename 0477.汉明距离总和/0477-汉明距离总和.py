class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ret = 0
        c0, c1 = 0, 0
        for i in range(30):
            for num in nums:
                if (num >> i) & 1 == 0:
                    c0 += 1
                else:
                    c1 += 1
            ret += c0 * c1
            c0, c1 = 0, 0
        return ret
