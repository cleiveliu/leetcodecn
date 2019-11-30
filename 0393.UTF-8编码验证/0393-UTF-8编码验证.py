class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def h(data, n):
            nonlocal index
            for _ in range(n):
                index += 1
                if not (
                    index < len(data) and bin(data[index])[2:].zfill(8)[:2] == "10"
                ):
                    return True
            index += 1
            return False

        index = 0
        while index < len(data):
            bnum = bin(data[index])[2:]
            bnum = bnum.zfill(8)
            if bnum.startswith("0"):
                index += 1
            elif bnum.startswith("110"):
                if h(data, 1):
                    return False
            elif bnum.startswith("1110"):
                if h(data, 2):
                    return False
            elif bnum.startswith(("11110")):
                if h(data, 3):
                    return False
            else:
                return False
        return True
