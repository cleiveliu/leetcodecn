# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre,fast,slow = None,head,head
        for _ in range(n):
            fast = fast.next
        while fast:
            pre,slow,fast = slow,slow.next,fast.next
        if slow == head:
            return head.next
        else:
            pre.next = slow.next
        return head
            
        
        """
        def get_len(head):
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret
        if not head:
            return None
        cur = head
        length = get_len(cur)
        cur = head
        if length == 1 and n ==1 :
            return None
        elif length == n:
            return head.next
        else:
            pre = None
            for _ in range(length-n):
                pre,cur = cur,cur.next
            pre.next = cur.next
            return head
        """
            