class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        mask16 = 0xFFFF
        mask8 = 0x00FF00FF
        mask4 = 0x0F0F0F0F
        mask2 = 0x33333333
        mask1 = 0x55555555
        tmp1 = ((n & mask1) << 1) | ((n >> 1) & mask1)
        tmp2 = ((tmp1 & mask2) << 2) | ((tmp1 >> 2) & mask2)
        tmp3 = ((tmp2 & mask4) << 4) | ((tmp2 >> 4) & mask4)
        tmp4 = ((tmp3 & mask8) << 8) | ((tmp3 >> 8) & mask8)
        tmp5 = ((tmp4 & mask16) << 16) | ((tmp4 >> 16) & mask16)
        return tmp5
