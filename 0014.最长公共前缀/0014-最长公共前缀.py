from itertools import takewhile


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return "".join(
            map(lambda xs: xs[0], takewhile(lambda xs: len(set(xs)) == 1, zip(*strs)))
        )
        # weird in python
