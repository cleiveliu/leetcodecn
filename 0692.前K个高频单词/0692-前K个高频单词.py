class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        ds = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        return [ds[i][0] for i in range(k)]