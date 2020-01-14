class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(map(lambda z: 1 if z[0] != z[1] else 0, zip(sorted(heights), heights)))