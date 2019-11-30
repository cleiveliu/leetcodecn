"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        ret = []
        if not root:
            return ret
        ret.append(root.val)
        for child in root.children:
            ret.extend(self.preorder(child))

        return ret
