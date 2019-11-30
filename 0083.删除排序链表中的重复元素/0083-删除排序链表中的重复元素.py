# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        while cur:
            while cur and pre.val == cur.val:
                cur = cur.next
            if not cur:
                pre.next = None
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        return head
