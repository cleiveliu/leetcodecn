class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        pre = 0
        index = len(A) - 1
        while K or pre:
            if K:
                if index >= 0:
                    temp = A[index]
                    A[index] = (A[index] + pre + K % 10) % 10
                    pre = (temp + pre + K % 10) // 10
                    index -= 1
                    K = K // 10
                else:
                    A.insert(0, (pre + K % 10) % 10)
                    pre = (pre + K % 10) // 10
                    K = K // 10
            else:
                if index >= 0:
                    temp = A[index]
                    A[index] = (A[index] + pre) % 10
                    pre = (pre + temp) // 10
                    index -= 1
                else:
                    A.insert(0, pre)
                    pre = 0
        return A
