# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        def get_len(head):
            return 0 if not head else 1 + get_len(head.next)
        cur = head
        n = get_len(cur)
        k = k%n
        if k == 0:
            return head
        slow,fast = head,head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow,fast = slow.next, fast.next
        ret = slow.next
        slow.next = None
        fast.next = head
        return ret
        
        
        