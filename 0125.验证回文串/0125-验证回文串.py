class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        s = "".join(
            map(lambda x: x.lower(), filter(lambda x: x.isalnum() or x.isalpha(), s))
        )
        return s == s[::-1]
