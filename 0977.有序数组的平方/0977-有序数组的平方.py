class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x: x * x, A))
