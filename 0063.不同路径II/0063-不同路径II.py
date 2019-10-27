class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        r,c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    grid[i][j] = '#'
                    
        
        i = 0
        while i < c:
            if grid[0][i] == '#':
                while i < c:
                    grid[0][i] = '#'
                    i += 1
            else:
                grid[0][i] = 1
                i += 1
        i = 1
        while i < r:
            if grid[i][0] == '#':
                while i < r:
                    grid[i][0] = '#'
                    i += 1
            else:
                grid[i][0] = 1
                i += 1
        
        for i in range(1,r):
            for j in range(1,c):
                if grid[i][j] == 0:
                    l = grid[i][j-1] if grid[i][j-1] != '#' else 0
                    u = grid[i-1][j] if grid[i-1][j] != '#' else 0
                    grid[i][j] = l + u
        return grid[-1][-1]
                