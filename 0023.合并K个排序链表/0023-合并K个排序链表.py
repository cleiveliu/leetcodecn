# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        def take_min(lists):
            for l in lists[:]:
                if not l:
                    lists.remove(l)
            if not lists:
                return None
            ret = 0
            for i,l in enumerate(lists):
                if l.val < lists[ret].val:
                    ret = i
            return ret
        while len(lists) > 1:
            min_ = take_min(lists)
            if min_ is not None:
                cur.next = lists[min_]
                cur = cur.next
                lists[min_]  = lists[min_].next
        if lists:
            cur.next = lists[0]
        return dummy.next