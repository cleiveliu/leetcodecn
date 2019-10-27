# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def merge(n1, n2):
            if not (n1 or n2):
                return None
            if n1 and n2:
                if n1.val < n2.val:
                    n1.next = merge(n1.next, n2)
                    return n1
                else:
                    n2.next = merge(n1, n2.next)
                    return n2
            return n1 or n2
        return merge(l1, l2)