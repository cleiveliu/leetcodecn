class Solution:
    def validTicTacToe(self, bd: List[str]) -> bool:
        xs = sum(map(lambda x: x.count('X'), bd))
        os = sum(map(lambda x: x.count('O'), bd))
        if xs < os or xs > os+1:
            return False
        def calc(bd, symbol):
            ret = 0
            ret += sum(map(lambda x: x==symbol*3, bd))
            ret += sum(map(lambda col: bd[0][col] == symbol and \
                                        bd[0][col] == bd[1][col] and \
                                        bd[1][col] == bd[2][col],
                                        range(3)))
            if bd[0][0] == symbol and bd[0][0] == bd[1][1] and bd[1][1] == bd[2][2]:
                ret += 1
            if bd[0][2] == symbol and bd[0][2] == bd[1][1] and bd[1][1] == bd[2][0]:
                ret += 1
            return ret
        x3 = calc(bd, 'X')
        o3 = calc(bd, 'O')
        if min(x3, o3) != 0:
            return False
        if o3 >= 1 and xs != os:
            return False
        if x3 >= 1 and xs != os + 1:
            return False
        return True
        