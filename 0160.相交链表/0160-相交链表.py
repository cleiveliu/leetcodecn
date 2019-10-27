# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def get_len(node):
            ret = 0
            cur = node
            while cur:
                ret += 1
                cur = cur.next
            return ret
        lena,lenb = get_len(headA), get_len(headB)
        cur1, cur2 = headA,headB
        if not cur1 or not cur2:
            return None
        diff = abs(lena-lenb)
        if lena > lenb:
            for _ in range(diff):
                cur1 = cur1.next
        else:
            for _ in range(diff):
                cur2 = cur2.next
        
        while cur1 and cur2:
            if cur1 is cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        return None