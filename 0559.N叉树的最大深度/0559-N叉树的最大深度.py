"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def to_childs(children):
            ret = []
            for child in children:
                ret.append(child)
            return ret
        def max_(arr):
            ret = 0
            for a in arr:
                if a > ret:
                    ret = a
            return ret
        def h(node):
            if not node:
                return 0
            return 1 + max_(map(h, to_childs(node.children)))
        return h(root)