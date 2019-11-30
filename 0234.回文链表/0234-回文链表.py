# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def to_arr(node):
            ret = []
            cur = node
            while cur:
                ret.append(cur.val)
                cur = cur.next
            return ret

        arr = to_arr(head)
        return arr == arr[::-1]
