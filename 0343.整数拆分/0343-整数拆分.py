class Solution:
    def integerBreak(self, n: int) -> int:
        # others solution

        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        
        n3, left = n//3, n%3

        if left  == 1:
            n3 -= 1
            left += 3
        elif left == 2:
            n3 -= 1
            left *= 3
        
        if left == 0:
            return 3**n3
        else:
            return (3**n3)*left
