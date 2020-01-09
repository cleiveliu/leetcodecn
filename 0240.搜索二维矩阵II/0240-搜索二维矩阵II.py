class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # from left_down to search
        if not matrix or not matrix[0]:
            return False
        
        i = len(matrix) - 1
        j = 0
        
        while i >= 0 and j < len(matrix[0]):
            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False