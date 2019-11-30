class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        vals = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        xs = [vals[c] for c in digits]

        def h(ret, xs, cur):
            if not xs:
                ret.append(cur)
                return
            for c in xs[0]:
                h(ret, xs[1:], cur + c)

        ret = []
        h(ret, xs, "")

        return ret
