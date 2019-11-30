class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = []
        for n in nums:
            if not stack or n > 0:
                stack.append(n)
            else:
                keep_n = True
                while stack and keep_n:
                    if stack[-1] > 0:
                        if stack[-1] < abs(n):
                            stack.pop()
                        elif stack[-1] == abs(n):
                            stack.pop()
                            keep_n = False
                        else:
                            keep_n = False
                    else:
                        break
                if keep_n:
                    stack.append(n)
        return stack
