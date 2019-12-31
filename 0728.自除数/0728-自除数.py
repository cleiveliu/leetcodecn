class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def get_nums(num):
            return list(map(int, str(num)))
        
        ret = []
        
        for i in range(left, right+1):
            if '0' in str(i):
                continue
                
            nums = get_nums(i)
            
            if all(i%num == 0 for num in nums):
                ret.append(i)
            
        
        return ret