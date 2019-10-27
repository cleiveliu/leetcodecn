# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def h(head):
            #reverse the list
            pre = None
            cur = head
            while cur.next:
                tem = cur
                cur = cur.next
                tem.next = pre
                pre = tem
            cur.next = pre
            return cur, head
        pre = None
        after = None
        cur = head
        i = 0
        start = None
        while cur:
            i += 1
            if i == m-1:
                pre = cur
            if i == m:
                start = cur
            if i == n:
                tem = cur
                after = cur.next
                tem.next = None
                break
            cur = cur.next
        mid_head, mid_tail = h(start)
        mid_tail.next = after
        if not pre:
            return mid_head
        else:
            pre.next = mid_head
            return head