class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def h (items,ret,path):
            if not items:
                ret.append(path)
                return
            for i,each in enumerate(items):
                h (items[:i]+items[i+1:],ret,path+[each])
        ret = []
        h (nums, ret, [])
        
        return ret
        