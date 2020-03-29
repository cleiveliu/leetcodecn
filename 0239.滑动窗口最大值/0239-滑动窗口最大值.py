from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Q()
        ret = [0]*( len(nums) - k + 1)

        for i in range(len(nums)):
            if i < k-1:
                q.push(nums[i])
            else:
                q.push(nums[i])
                ret[i-k+1] = q.max()
                q.pop(nums[i-k+1])
                
        return ret

class Q:
    def __init__(self):
        self.q = deque()
    def push(self, val):
        while len(self.q) > 0 and self.q[0] < val:
            self.q.popleft()
        self.q.appendleft(val)
    def max(self):
        if len(self.q) > 0:
            return self.q[-1]
    def pop(self, val):
        if len(self.q) > 0 and self.q[-1] == val:
            self.q.pop()
        