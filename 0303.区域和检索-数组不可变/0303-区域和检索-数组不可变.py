class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        def x(arr,pre = 0):
            ret = [0]*len(arr)
            if len(arr) == 0:
                return ret
            ret[0] = arr[0]
            for i,num in enumerate(arr[1:], start=1):
                ret[i] = num + ret[i-1]
            return ret
        self.cache = x(self.nums)
            
        

    def sumRange(self, i: int, j: int) -> int:
        return self.cache[j] - self.cache[i-1] if i != 0 else self.cache[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)