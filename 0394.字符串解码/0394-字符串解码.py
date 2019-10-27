class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        str_nums = ''.join(map(str,range(10)))
        for c in s:
            if c == ']':
                tem = ''
                p = stack.pop()
                while p != '[':
                    tem = p + tem
                    p = stack.pop()
                if stack:
                    n = ''
                    while stack and stack[-1] in str_nums:
                        n = stack.pop() + n
                    if n:
                        n = int(n)
                        tem = tem*n
                stack.append(tem)
            else:
                stack.append(c)
        return ''.join(stack)