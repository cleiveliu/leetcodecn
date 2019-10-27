# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def h(pre,node):
            if not node:
                return pre
            temp = node.next
            node.next = pre
            return h(node, temp)
        return h(None, head)
        