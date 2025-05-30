/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_map<ListNode*,int>mpp;
    for (auto p = headA ; p!=NULL ; p = p->next){
        mpp[p]=p->val;
    }
    for (auto p = headB ; p!=NULL ; p = p->next){
        if (mpp.find(p)!=mpp.end()) return p;
    }
    return NULL;
    }
};