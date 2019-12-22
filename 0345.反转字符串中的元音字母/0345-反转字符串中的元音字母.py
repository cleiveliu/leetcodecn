class Solution:
    def reverseVowels(self, s: str) -> str:
        targets = "aeiouAEIOU"
        chars = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if chars[i] in targets and chars[j] in targets:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
            while i < len(chars) and chars[i] not in targets:
                i += 1
            while j >= 0 and chars[j] not in targets:
                j -= 1
        return "".join(chars)
