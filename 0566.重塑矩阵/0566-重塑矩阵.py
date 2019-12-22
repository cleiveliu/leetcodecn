class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:

        if not nums or not nums[0]:
            return nums

        row, col = len(nums), len(nums[0])
        if row * col != r * c:
            return nums

        new = [[0] * c for _ in range(r)]
        indexr, indexc = 0, 0
        for i in range(row):
            for j in range(col):
                new[indexr][indexc] = nums[i][j]
                indexc = (indexc + 1) % c
                if indexc == 0:
                    indexr = (indexr + 1) % r
        return new
