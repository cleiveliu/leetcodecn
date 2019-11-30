"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            new_stack = []
            vals = []
            while stack:
                node = stack.pop(0)
                vals.append(node.val)
                new_stack.extend(node.children)
            stack = new_stack
            ret.append(vals)
        return ret
