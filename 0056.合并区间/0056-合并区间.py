class Solution:  # intervals
    def merge(self, pairs: List[List[int]]) -> List[List[int]]:
        if not pairs:
            return []
        pairs.sort(key=lambda x: x[0])
        ret = [pairs[0]]
        for l, r in pairs:
            if l > ret[-1][1]:
                ret.append([l, r])
            else:
                ret[-1][1] = max(ret[-1][1], r)
        return ret
