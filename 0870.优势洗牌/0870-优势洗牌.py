class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        B = [(n,i) for i,n in enumerate(B)]
        B.sort(key=lambda x: x[0])
        temp = []
        ret = [-1]*len(A)
        i,j = 0,0
        while i < len(A) and j < len(B):
            n,index = B[j]
            if A[i] > n:
                ret[index] = A[i]
                i += 1
                j += 1
            else:
                temp.append(A[i])
                i += 1
        index = 0
        while temp:
            while index < len(ret) and ret[index] != -1:
                index += 1
            if index < len(ret):
                ret[index] = temp.pop()
        return ret