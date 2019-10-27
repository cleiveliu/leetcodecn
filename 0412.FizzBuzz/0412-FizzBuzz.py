class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = list(map(str,range(1,n+1)))
        for index in range(2,n,3):
            ret[index] = "Fizz"
        for index in range(4,n,5):
            ret[index] = "Buzz"
        for index in range(14,n,15):
            ret[index] = "FizzBuzz"
        return ret