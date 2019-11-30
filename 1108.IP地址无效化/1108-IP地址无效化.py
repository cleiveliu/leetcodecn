class Solution:
    def defangIPaddr(self, addr: str) -> str:
        return "[.]".join(addr.split("."))
