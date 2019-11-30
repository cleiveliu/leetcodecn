class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def h(arr, cur, k, ret):
            if len(cur) == k:
                ret.append(cur)
                return
            for i, num in enumerate(arr):
                h(arr[i + 1 :], cur + [num], k, ret)
                # h(arr[i+1:], cur, k, ret)

        ret = []
        h(list(range(1, n + 1)), [], k, ret)

        return ret
