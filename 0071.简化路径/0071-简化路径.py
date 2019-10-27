class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split('/')
        stack = []
        for c in split:
            if c == '..':
                if stack:
                    stack.pop()
            elif c != '' and c != '.':
                stack.append(c)
        return '/' + '/'.join(stack)
        