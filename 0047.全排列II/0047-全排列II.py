class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def h (items, ret, path):
            if not items:
                ret.append(path)
                return
            for i,each in enumerate(items):
                if i-1 >= 0 and items[i-1] == items[i]:
                    continue
                h (items[:i]+items[i+1:], ret, path+[each])
        nums.sort()
        ret = []
        h (nums, ret, [])
        return ret
        