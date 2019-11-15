class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        area = 0
        #bottom area
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    area += 1
        
        for i in range(row):
            area += max(grid[i])
        
        for i in range(col):
            max_ = grid[0][i]
            for j in range(row):
                max_ = max(max_, grid[j][i])
            area += max_
        return area