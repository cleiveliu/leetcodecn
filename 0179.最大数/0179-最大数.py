class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        chars = list(map(str, nums))
        
        for i in range(len(chars) - 1):
            for j in range(i+1, len(chars)):
                if chars[i] + chars[j]  < chars[j] + chars[i]:
                    chars[i], chars[j] = chars[j], chars[i]
        
        return ''.join(chars) if chars[0] != '0' else '0'