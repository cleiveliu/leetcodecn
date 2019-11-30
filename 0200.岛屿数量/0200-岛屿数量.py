class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark(grid, i, j):
            if grid[i][j] == "1":
                grid[i][j] = "N"
                r, c = len(grid), len(grid[0])
                for dx, dy in get_ds(i, j, r, c):
                    mark(grid, dx, dy)

        def get_ds(i, j, r, c):
            ret = []
            if i - 1 >= 0:
                ret.append((i - 1, j))
            if i + 1 < r:
                ret.append((i + 1, j))
            if j - 1 >= 0:
                ret.append((i, j - 1))
            if j + 1 < c:
                ret.append((i, j + 1))
            return ret

        if not grid:
            return 0

        ret = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    ret += 1
                    mark(grid, i, j)
        return ret
