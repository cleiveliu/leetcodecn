class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        temp = sorted(d.items(), key=lambda x: x[1], reverse=True)
        ret = []
        for i in range(k):
            ret.append(temp[i][0])
        return ret
