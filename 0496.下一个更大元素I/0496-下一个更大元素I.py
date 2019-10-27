class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for num in nums2:
            for key in d.keys():
                if d[key] == -1 and num > key:
                    d[key] = num
            d[num] = -1
        ret = [0]*len(nums1)
        for i,n in enumerate(nums1):
            ret[i] = d.get(n,0)
        return ret
            