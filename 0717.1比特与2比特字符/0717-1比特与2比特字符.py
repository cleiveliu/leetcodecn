class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        def count1(bits):
            ret = 0
            index = len(bits)-1
            while index >= 0 and bits[index] == 1:
                ret += 1
                index -= 1
            return ret

        n = count1(bits[:-1])

        return True if n % 2 == 0 else False