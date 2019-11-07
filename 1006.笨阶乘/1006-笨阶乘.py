class Solution:
    def clumsy(self, N: int) -> int:
        def take4_or_less(n):
            xs = []
            while n >= 1 and len(xs) < 4:
                xs.append(n)
                n -= 1
            return xs, n
        def calc4_or_less(xs):
            if len(xs) == 4:
                x1,x2,x3,x4 = xs
                return x1*x2//x3+x4
            elif len(xs) == 3:
                x1,x2,x3 = xs
                return x1*x2//x3
            elif len(xs) == 2:
                x1,x2 = xs
                return x1*x2
            elif len(xs) == 1:
                return xs[0]
            else:
                return 0
        xs, N = take4_or_less(N)
        ret = calc4_or_less(xs)
        while N >= 1:
            xs,N = take4_or_less(N)
            #print(xs,N)
            if len(xs) == 4:
                ret -= calc4_or_less(xs[:-1])
                ret += xs[-1]
            else:
                ret -= calc4_or_less(xs)
        return ret