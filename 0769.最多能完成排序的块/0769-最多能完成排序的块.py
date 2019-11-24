class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ret = 0
        until_index = 0
        for index,num in enumerate(arr):
            until_index = max(until_index, arr[index])
            if index == until_index:
                ret += 1
        return ret
            