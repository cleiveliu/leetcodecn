class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def contains_sub(s,t):
            index_s = 0
            index_t = 0
            while index_t < len(t) and index_s < len(s):
                while index_t < len(t) and index_s < len(s) and t[index_t] == s[index_s]:
                    index_s += 1
                    index_t += 1
                index_s += 1
            
            return index_t >= len(t)
        d = dict()
        for s in strs:
            d[s] = d.get(s, 0) + 1
        keys = [key for key,val in d.items() if val == 1]
        keys.sort(key = lambda x:len(x), reverse=True)
        for key in keys:
            len_gt_keys = filter(lambda x:len(x) > len(key), strs)
            if all( not contains_sub(x,key) for x in len_gt_keys):
                return len(key)
        
        
        
        return -1