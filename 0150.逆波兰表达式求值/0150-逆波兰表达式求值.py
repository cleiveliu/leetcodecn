class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+':lambda x,y: x + y,
            '-':lambda x,y: x - y,
            '*':lambda x,y: x * y,
            '/':lambda x,y: int(x/y),
        }
        def get_2num(stack):
            r = stack.pop()
            l = stack.pop()
            return l,r
        stack = []
        for t in tokens:
            if t in ops:
                n = ops[t](*get_2num(stack))
                stack.append(n)
            else:
                n = int(t)
                stack.append(n)
        return stack[-1]