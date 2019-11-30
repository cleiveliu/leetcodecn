import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # no more duplicated wheels ,Dog
        return bool(re.fullmatch(p, s))
