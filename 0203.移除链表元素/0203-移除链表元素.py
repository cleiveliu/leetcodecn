# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def remove(node, target):
            if not node:
                return None
            elif node.val == target:
                return remove(node.next, target)
            else:
                node.next = remove(node.next, target)
                return node

        return remove(head, val)
