# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        stack = [root]
        is_last = False # bottom level
        level = 0
        while stack:
            if is_last:
                if any(node.left or node.right for node in stack):
                    return False
                else:
                    return True
            if not is_last and len(stack) != 2**level:
                return False
            
            new_stack = []
            while stack:
                node = stack.pop(0)
                if node.left and node.right:
                    new_stack.append(node.left)
                    new_stack.append(node.right)
                else:
                    is_last = True
                    if not node.left and node.right:
                        return False
                    elif any(node.left or node.right for node in stack):
                        return False
                    else:
                        if node.left:
                            new_stack.append(node.left)
                        if node.right:
                            new_stack.append(node.right)
            stack = new_stack
            level += 1
        return True
                    