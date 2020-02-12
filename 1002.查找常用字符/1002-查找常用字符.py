class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        def count(word):
            d = {}
            for w in word:
                d[w] = d.get(w, 0) + 1
            return d
        def update_map(d, tem):
            ret = {}
            for key, val in tem.items():
                ret[key] = min(d.get(key, 0), val)
            return ret
        
        m = count(A[0])

        for word in A[1:]:
            tem = count(word)
            m = update_map(m, tem)
        
        ret = []
        for key, val in m.items():
            for _ in range(val):
                ret.append(key)
        
        return ret