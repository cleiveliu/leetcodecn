class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        all_cubic = sum(map(sum,grid))
        e = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])-1):
                e += min(grid[i][j],grid[i][j+1])
        for i in range(len(grid[0])):
            for j in range(len(grid)-1):
                e += min(grid[j][i],grid[j+1][i])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                e += max(0,grid[i][j]-1)
        return all_cubic*6 - e*2
                