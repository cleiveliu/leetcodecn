class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        j = 1
        for i in range(0, len(A), 2):
            if A[i] & 1 == 1:
                while A[j] & 1 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        
        return A

        """
        odds = [a for a in A if a & 1 == 1]
        evens = [a for a in A if a & 1 == 0]

        A[::2] = evens
        A[1::2] = odds

        return A
        """