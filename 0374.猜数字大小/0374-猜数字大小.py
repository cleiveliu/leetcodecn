# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        g = (l + r) // 2
        while guess(g) != 0:
            if guess(g) == 1:
                l = g + 1
            else:
                r = g - 1

            g = (l + r) // 2
        return g
