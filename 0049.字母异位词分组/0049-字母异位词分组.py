class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        ret = []
        index = 0
        for word in strs:
            s = ''.join(sorted(word))
            if s in d:
                ret[d[s]].append(word)
            else:
                d[s] = index
                index += 1
                ret.append([word])
        return ret
                
        