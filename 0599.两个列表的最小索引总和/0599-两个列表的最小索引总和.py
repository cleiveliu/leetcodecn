class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        d = {}
        for i, a in enumerate(list1):
            if a in common:
                d[a] = i
        for i, a in enumerate(list2):
            if a in common:
                d[a] += i

        tem = sorted(d.items(), key=lambda x: x[1])
        k, val = tem[0]
        ret = [k]
        for k, v in tem[1:]:
            if v == val:
                ret.append(k)
            else:
                return ret
        return ret
