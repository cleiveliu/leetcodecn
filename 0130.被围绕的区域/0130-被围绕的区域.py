class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def mark(grid, i, j):
            # mark not surrounded point to "N"
            if grid[i][j] == 'O':
                grid[i][j] = 'N'
                r,c =len(grid), len(grid[0])
                for dx,dy in get_ds(i,j,r,c):
                    mark(grid, dx, dy)
        
        def get_ds(i,j,r,c):
            ret = []
            if i-1 >= 0:
                ret.append((i-1,j))
            if i+1 < r:
                ret.append((i+1,j))
            if j-1 >= 0:
                ret.append((i,j-1))
            if j+1 < c:
                ret.append((i,j+1))
            return ret
        
        if not board:
            return
        
        r,c =len(board), len(board[0])
        
        for i in range(c):
            if board[0][i] == 'O':
                mark(board,0,i)
            if board[r-1][i] == 'O':
                mark(board,r-1,i)
        for i in range(r):
            if board[i][0] == 'O':
                mark(board,i,0)
            if board[i][c-1] == 'O':
                mark(board,i,c-1)
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
            
        