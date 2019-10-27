class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l, r = 0,0
        stack = []
        for c in S:
            if l == 0:
                l += 1
            elif c == '(':
                l += 1
                stack.append(c)
            elif c == ')':
                r += 1
                if l != r:
                    stack.append(c)
                else:
                    l, r = 0,0
        return ''.join(stack)