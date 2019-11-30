class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ret = [0] * len(T)
        stack = []
        for i in range(len(T)):
            if not stack:
                stack.append((T[i], i))
            else:
                while stack and T[i] > stack[-1][0]:
                    _, index = stack.pop()
                    ret[index] = i - index
                stack.append((T[i], i))
        return ret
