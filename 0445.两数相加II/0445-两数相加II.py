# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def to_arr(list_):
            ret = []
            cur = list_
            while cur:
                ret.append(cur.val)
                cur = cur.next
            return ret

        a1 = to_arr(l1)
        a2 = to_arr(l2)
        i, j = len(a1) - 1, len(a2) - 1
        ret = []
        rem = 0
        while i >= 0 and j >= 0:
            ret.append((a1[i] + a2[j] + rem) % 10)
            rem = (a1[i] + a2[j] + rem) // 10
            i -= 1
            j -= 1
        while i >= 0:
            ret.append((a1[i] + rem) % 10)
            rem = (a1[i] + rem) // 10
            i -= 1
        while j >= 0:
            ret.append((a2[j] + rem) % 10)
            rem = (a2[j] + rem) // 10
            j -= 1
        if rem > 0:
            ret.append(rem)
        dummy = ListNode(0)
        cur = dummy
        for val in ret[::-1]:
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        return dummy.next
