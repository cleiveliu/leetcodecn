class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0  # 挨着的边
        num = 0  # numbers of 1
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    num += 1
        for i in range(r):
            for j in range(c - 1):
                if grid[i][j] == 1 and grid[i][j + 1] == 1:
                    cnt += 1
        for i in range(c):
            for j in range(r - 1):
                if grid[j][i] == 1 and grid[j + 1][i] == 1:
                    cnt += 1

        return 4 * num - 2 * cnt
