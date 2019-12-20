from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_place(row, col):
            return cols[col] == 0 and lu_rd[row - col] == 0 and ld_ru[row + col] == 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                chars = "." * col + "Q" + "." * (n - col - 1)
                solution.append(chars)
            ret.append(solution)

        def add_queen(row, col):
            t = (row, col)
            queens.add(t)
            cols[col] = 1
            lu_rd[row - col] = 1
            ld_ru[row + col] = 1

        def romove_queen(row, col):
            t = (row, col)
            queens.remove(t)
            cols[col] = 0
            lu_rd[row - col] = 0
            ld_ru[row + col] = 0

        def backtrack(row=0):
            for col in range(n):
                if can_place(row, col):
                    add_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    romove_queen(row, col)

        cols = [0] * (n + 1)
        lu_rd = [0] * (n * 2 + 1)  # left-up to right-down
        ld_ru = [0] * (n * 2 + 1)  # left-down to right-up
        queens = set()
        ret = []

        backtrack()

        return ret