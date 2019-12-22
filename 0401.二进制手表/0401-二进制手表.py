class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def gen(base, n, index, ret):
            # where n <= len(base)
            if n == 0:
                ret.append(base)
                return
            if index >= len(base):
                return
            new_base = base.copy()
            new_base[index] = True
            gen(base, n, index + 1, ret)
            gen(new_base, n - 1, index + 1, ret)

        def base_to_num(base):
            # where base: [bool]
            ret = 0
            for i, n in enumerate(base[::-1]):
                ret += 2 ** i * n
            return ret

        def two_num_to_time(n1, n2):
            # where 0<= n1 <= 11    0<= n2 <= 59
            return str(n1) + ":" + ("0" + str(n2) if n2 < 10 else str(n2))

        ret = []
        for i in range(num + 1):
            up = i
            down = num - i
            up_bases = []
            gen([False] * 4, up, 0, up_bases)
            down_bases = []
            gen([False] * 6, down, 0, down_bases)
            up_bases = map(base_to_num, up_bases)
            up_bases = list(filter(lambda x: 0 <= x <= 11, up_bases))
            down_bases = map(base_to_num, down_bases)
            down_bases = list(filter(lambda x: 0 <= x <= 59, down_bases))

            for n1 in up_bases:
                for n2 in down_bases:
                    time = two_num_to_time(n1, n2)
                    ret.append(time)
        return ret
