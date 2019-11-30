class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_rest = 0  # from index 0
        cur_rest = 0  # from index i
        start = 0
        for i in range(len(gas)):
            total_rest += gas[i] - cost[i]
            cur_rest += gas[i] - cost[i]
            if cur_rest < 0:
                start = i + 1
                cur_rest = 0
        return -1 if total_rest < 0 else start % len(gas)
