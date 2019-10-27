class Solution:
    def convert(self, s: str, n: int) -> str:
        if not s or len(s) < 2 or n == 1:
            return s
        single_c = n-1
        r = n
        c = int(len(s) // (n + n-2)) + 1
        grid = [[None]*(c*single_c) for _ in range(r)]
        def walk(grid,r,i,j,s):
            index = 0
            len_ = len(s)
            for _ in range(r):
                if index < len_:
                    grid[i][j] = s[index]
                    i += 1
                    index += 1
            i -= 1
            for _ in range(r-2):
                i -= 1
                j += 1
                if index < len_:
                    grid[i][j] = s[index]
                    index += 1
        step = n + (n-2)
        c_step = n-1
        cc = 0
        for i in range(0,len(s),step):
            walk(grid,n,0,cc,s[i:i+step])
            cc += c_step
        #print(grid)
        def h(xs):
            return ''.join(filter(lambda x: x is not None, xs))
        return ''.join(map(h,grid))
            
                