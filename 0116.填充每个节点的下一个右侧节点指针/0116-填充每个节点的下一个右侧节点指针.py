"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = [root]
        while stack:
            new_stack = []
            if len(stack) > 1:
                for i in range(len(stack)-1):
                    stack[i].next = stack[i+1]
            while stack:
                node = stack.pop(0)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
        return root