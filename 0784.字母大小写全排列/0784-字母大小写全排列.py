import string


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        lowers = string.ascii_lowercase
        uppers = string.ascii_uppercase
        letters = set(lowers + uppers)

        def trans(char):
            if char in lowers:
                return uppers[lowers.index(char)]
            else:
                return lowers[uppers.index(char)]

        def gen(arr, n, ret):
            if n >= len(arr):
                ret.append(arr)
            else:
                new_arr = arr.copy()
                gen(arr, n + 1, ret)
                new_arr[n] = True
                gen(new_arr, n + 1, ret)

        def exchange(chars, arr):
            return "".join(
                trans(char) if flag else char for char, flag in zip(chars, arr)
            )

        def recombi(chars, arr, indexs):
            for index, char in zip(indexs, chars):
                arr[index] = char
            return "".join(arr)

        chars = "".join(filter(lambda x: x in letters, S))
        indexs = list((i for i, x in enumerate(S) if x in letters))
        arr = list(S)
        # print(chars, indexs, arr)
        if len(chars) == 0:
            return [S]
        else:
            n = len(chars)
            combs = []
            gen([False] * n, 0, combs)
            combs = list((exchange(chars, comb) for comb in combs))
            ret = []
            for recomb in (recombi(comb, arr, indexs) for comb in combs):
                ret.append(recomb)
            return ret
