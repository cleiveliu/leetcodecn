class Solution:
    def calculate(self, s: str) -> int:
        def calc_stack(stack):
            if all(map(is_atom,stack)):
                return calc(stack)
            else:
                for i,s in enumerate(stack):
                    if not is_atom(s):
                        stack[i] = calc_stack(stack[i])
                return calc(stack)
        
        def calc(arr):
            if len(arr) == 1:
                return arr[0]
            l,op,r = arr[:3]
            l,r = int(l),int(r)
            if op == '+':
                return calc( [l+r] + arr[3:] )
            elif op == '-':
                return calc( [l-r] + arr[3:] )
                
        def is_atom(s):
            return not isinstance(s,list)
        
        def to_stack(s,ret,i):
            while i < len(s):
                c = s[i]
                if c.isalnum():
                    tem = c
                    while i + 1 < len(s) and s[i+1].isalnum():
                        tem += s[i+1]
                        i += 1
                    ret.append(int(tem))
                elif c in '+-':
                    ret.append(c)
                elif c == '(':
                    stack,i = to_stack(s,[],i+1)
                    ret.append(stack)
                elif c == ')':
                    return ret,i
                i += 1
            return ret
        stack = to_stack(s,[],0)
        ret = calc_stack(stack)
        return ret
                    
                    