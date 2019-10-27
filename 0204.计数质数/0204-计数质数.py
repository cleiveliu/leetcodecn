class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        arr = [True]*n
        index = 2
        while index < int(n**0.5)+1:
            if arr[index] == True:
                step = index
                cur = index + step
                while cur < n:
                    arr[cur] = False
                    cur += step
            index += 1
        return sum(arr[2:])

        
                    
        