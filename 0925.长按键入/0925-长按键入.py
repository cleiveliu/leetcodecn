class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        slow, fast = 0, 0
        while slow < len(name) and fast < len(typed):
            if name[slow] == typed[fast]:
                slow += 1
                fast += 1
            else:
                fast += 1
        return slow == len(name)
