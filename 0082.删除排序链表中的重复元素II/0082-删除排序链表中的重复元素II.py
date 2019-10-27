# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        cur = dummy
        pre = [head,True]
        head = head.next
        while head:
            if head.val == pre[0].val:
                pre[1] = False
            else:
                if pre[1]:
                    cur.next = pre[0]
                    cur = cur.next
                    pre = [head,True]
                else:
                    pre = [head,True]
                    #print(pre[0].val,pre[1])
            head = head.next
        
        #print(pre[0].val,pre[1])
        if pre[1]:
            cur.next = pre[0]
        else:
            cur.next = None
        return dummy.next
        
                    