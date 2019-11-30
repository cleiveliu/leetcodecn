class Solution:
    def integerReplacement(self, n: int) -> int:
        def h(arr, ret):
            new_arr = []
            for a in arr:
                if a == 1:
                    return ret
                if a % 2 == 0:
                    new_arr.append(a // 2)
                else:
                    new_arr.append(a + 1)
                    new_arr.append(a - 1)
            return h(new_arr, ret + 1)

        nums = [n]
        return h(nums, 0)
