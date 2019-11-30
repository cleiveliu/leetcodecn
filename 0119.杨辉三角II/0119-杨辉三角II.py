class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        if n == 1:
            return [1, 1]
        pre = [1, 1]
        ret = []
        for _ in range(n - 1):
            len_ = len(pre) + 1
            ret = [1] * len_
            for i in range(1, len(ret) - 1):
                ret[i] = pre[i] + pre[i - 1]
            pre = ret[:]
        return ret
