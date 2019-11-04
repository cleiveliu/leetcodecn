/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int c;
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    if (l1==NULL&&l2==NULL&&c==0) return NULL;
    l1!=NULL? (c += l1->val, l1 = l1->next): (c += 0);
    l2!=NULL? (c += l2->val, l2 = l2->next): (c += 0);
    struct ListNode* p = (struct ListNode *)malloc(sizeof(struct ListNode));
    p->val = c%10;
    c  = c / 10;
    p->next = addTwoNumbers(l1, l2);
    return p;
}