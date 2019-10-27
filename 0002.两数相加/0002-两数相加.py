# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        flag = 0
        while l1 and l2:
            val = (l1.val+l2.val+flag)%10
            cur.next = ListNode(val)
            cur = cur.next
            flag = (l1.val+l2.val+flag)//10
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = (l1.val+flag)%10
            cur.next = ListNode(val)
            cur = cur.next
            flag = (l1.val+flag)//10
            l1 = l1.next
        while l2:
            val = (l2.val+flag)%10
            cur.next = ListNode(val)
            cur = cur.next
            flag = (l2.val+flag)//10
            l2 = l2.next
        while flag:
            val = flag%10
            cur.next = ListNode(val)
            cur = cur.next
            flag = flag//10
            
        return dummy.next
        """
        n1,n2 = 0,0
        flag = 0
        while l1:
            n1 += l1.val*(10**flag)
            l1 = l1.next
            flag += 1
        flag = 0
        while l2:
            n2 += l2.val*(10**flag)
            l2 = l2.next
            flag += 1
        n = n1 + n2
        #print(n)
        dummy = ListNode(0)
        cur = dummy
        if not n:
            return dummy
        while n:
            cur.next = ListNode(n%10)
            n = n//10
            cur = cur.next
        return dummy.next
        """
            
        