class Solution:
    def divide(self, a: int, b: int) -> int:
        def div(a, b, cur):
            if a < b:
                return cur
            ret = 1
            tmp = b
            while mul2(tmp) < a:
                ret = mul2(ret)
                tmp = mul2(tmp)
            cur = cur + ret
            if cur > 2**31-1:
                return 2**31-1
            elif cur < -2**31:
                return -2**31
            else:
                return div(a-tmp,b,cur)
        def mul2(x):
            return x + x
        
        flag = (a>0 and b>0) or (a<0 and b<0)
        
        a,b = abs(a),abs(b)
        
        ret = div(a, b, 0)
        if ret == 2**31-1 and not flag:
            return -2**31
        if ret == -2**31 and not not flag:
            return 2**31-1
        
        return ret if flag else 0-ret