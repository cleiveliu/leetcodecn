class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def p(xs, cur, n):
            if len(cur) == n:
                ret[0] += 1
                return
            for i,c in enumerate(xs):
                if i > 0 and xs[i] == xs[i-1]:
                    continue
                p(xs[:i]+xs[i+1:], cur+xs[i], n)
        ret = [0]
        tiles = ''.join(sorted(tiles))
        for i in range(1, len(tiles)+1):
            p(tiles, "", i)
        
        return ret[0]