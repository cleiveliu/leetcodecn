"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        ret = []
        if not root:
            return ret
        for child in root.children:
            ret.extend(self.postorder(child))
        ret.append(root.val)

        return ret
