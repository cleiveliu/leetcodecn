class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        for i in range(len(time)):
            time[i] = time[i] % 60
        d = {}
        ret = 0
        for t in time:
            if t in d:
                ret += d[t]
                d[(60 - t) % 60] = d.get((60 - t) % 60, 0) + 1
            else:
                d[(60 - t) % 60] = d.get((60 - t) % 60, 0) + 1
        return ret
