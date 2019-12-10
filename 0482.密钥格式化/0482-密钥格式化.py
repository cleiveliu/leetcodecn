class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        chars = ''.join(S.split('-'))
        # chars = ''.join(c.upper() for c in chars)
        chars = chars.upper()
        # print(chars)
        return '-'.join(reversed(list((chars[n-K:n] if n-K >= 0 else chars[0:n]
                                for n in range(len(chars),0,-K)))))