# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow ,fast = head,head
        while fast.next and fast.next.next:
            slow  = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        node1 = self.sortList(head)
        node2 = self.sortList(head2)
        
        return self._merge(node1, node2)
    def _merge(self,node1, node2):
        # where node1 node2: sorted :)
        if not node1:
            return node2
        if not node2:
            return node1
        if node1.val < node2.val:
            node1.next = self._merge(node1.next, node2)
            return node1
        else:
            node2.next = self._merge(node1, node2.next)
            return node2
        
        