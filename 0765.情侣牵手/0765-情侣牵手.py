class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def expectedfor(n):
            if n & 1 == 0:
                return n + 1
            else:
                return n - 1
        num_index = dict()
        for index, num in enumerate(row):
            num_index[num] = index
            
        ret = 0
        for i in range(0, len(row), 2):
            n = expectedfor(row[i])
            if row[i+1] != n:
                index = num_index[n]
                row[i+1], row[index] = row[index], row[i+1]
                num_index[row[index]] = index
                ret += 1
        
        return ret

            