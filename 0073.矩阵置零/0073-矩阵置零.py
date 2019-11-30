class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rc = [1] * 2  # record if the first row and col should be set to 0
        if 0 in matrix[0]:
            rc[0] = 0
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                rc[1] = 0
                break
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        def set_x(matrix, x):
            for i in range(len(matrix[0])):
                matrix[x][i] = 0

        def set_y(matrix, y):
            for i in range(len(matrix)):
                matrix[i][y] = 0

        for i in range(1, r):
            if matrix[i][0] == 0:
                set_x(matrix, i)
        for i in range(1, c):
            if matrix[0][i] == 0:
                set_y(matrix, i)
        if rc[0] == 0:
            set_x(matrix, 0)
        if rc[1] == 0:
            set_y(matrix, 0)
