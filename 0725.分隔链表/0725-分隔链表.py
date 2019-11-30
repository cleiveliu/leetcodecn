# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        def get_len(node):
            if node is None:
                return 0
            return 1 + get_len(node.next)

        cur = head
        len_ = get_len(cur)

        ret = []
        base = len_ // k
        plus = len_ - (base * k)

        cur = head
        for _ in range(k):
            tem = cur
            pre = None
            for _ in range(base):
                if cur:
                    pre = cur
                    cur = cur.next
            if plus > 0:
                pre = cur
                cur = cur.next
                plus -= 1
            if pre:
                pre.next = None
            ret.append(tem)
        return ret
