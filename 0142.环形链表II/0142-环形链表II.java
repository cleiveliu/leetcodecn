/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        Set<ListNode> visited = new HashSet<ListNode>();
        ListNode cur = head;
        while (cur != null) {
            if (visited.contains(cur)) {
                return cur;
            }
            visited.add(cur);
            cur = cur.next;
        }
        return null;
    }
}