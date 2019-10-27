class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack = []
        for c in s:
            if c in d:
                if not stack or stack.pop() != d[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0