/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        int lena = getLen(headA);
        int lenb = getLen(headB);
        int diff = Math.abs(lena-lenb);
        ListNode cur1 = headA;
        ListNode cur2 = headB;
        if (lena > lenb) {
            for (int i=0; i < diff; i++) {
                cur1 = cur1.next;
            }
        }
        if (lenb > lena) {
            for (int i=0; i < diff; i++) {
                cur2 = cur2.next;
            }
        }
        
        while (cur1 != null && cur2 != null) {
            if (cur1 == cur2) {
                return cur1;
            }
            cur1 = cur1.next;
            cur2 = cur2.next;
        }
        
        return null;
    }
    
    public int getLen(ListNode node) {
        int ret = 0;
        ListNode cur = node;
        while (cur != null) {
            ret += 1;
            cur = cur.next;
        }
        return ret;
    }
    
}