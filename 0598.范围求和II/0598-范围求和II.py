class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        return min(map(lambda x: x[0], ops)) * \
                min(map(lambda x: x[1], ops)) \
                if len(ops) > 0 and len(ops[0]) > 1 \
                else m*n