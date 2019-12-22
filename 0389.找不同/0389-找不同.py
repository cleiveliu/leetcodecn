class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr1 = [0] * 26
        arr2 = [0] * 26
        for c in s:
            arr1[ord(c) - 97] += 1  # ord('a') = 97
        for c in t:
            arr2[ord(c) - 97] += 1

        for i in range(26):
            if arr1[i] != arr2[i]:
                return chr(i + 97)

        """better version
        n = 0
        for c in s:
            n ^= ord(c)
        for c in t:
            n ^= ord(c)
        return chr(n)
        """
