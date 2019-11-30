class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        ret = [[1]]
        for i in range(2, n + 1):
            tem = []
            last = ret[-1]
            tem.append(1)
            for j in range(1, i - 1):
                tem.append(last[j] + last[j - 1])
            tem.append(1)
            ret.append(tem)
        return ret
