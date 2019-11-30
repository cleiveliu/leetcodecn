# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        elif not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        first, second = head, head.next
        while first and second:
            tem = second.next
            pre.next = second
            second.next = first
            first.next = tem
            first, second = second, first
            if second.next:
                for _ in range(2):
                    pre, first, second = pre.next, first.next, second.next
            else:
                break
        return dummy.next
