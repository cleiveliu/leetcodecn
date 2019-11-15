class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int( ''.join(map(lambda x: '1' if x == '0' else '0', bin(N)[2:])),
                  2)