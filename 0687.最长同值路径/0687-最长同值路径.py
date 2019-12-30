# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        self.max_len = 0
        
        def h(node):
            if node:
                left_num, left_count = h(node.left)
                right_num, right_count = h(node.right)
                if node.val == left_num and node.val == right_num:
                    self.max_len = max(self.max_len, (left_count+right_count+2))
                    return node.val, max(left_count, right_count) + 1
                elif node.val == left_num:
                    self.max_len = max(self.max_len, right_count)
                    return node.val, left_count+1
                elif node.val == right_num:
                    self.max_len = max(self.max_len, left_count)
                    return node.val, right_count+1
                else:
                    self.max_len = max(self.max_len, left_count, right_count)
                    return node.val, 0
            else:
                return None,0
        
        _, ret = h(root)
        
        return max(ret, self.max_len)