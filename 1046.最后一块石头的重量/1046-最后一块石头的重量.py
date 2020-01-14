class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            n = stones.pop() - stones.pop()
            if n != 0:
                stones.append(n)
        return 0 if len(stones) == 0 else stones[0]