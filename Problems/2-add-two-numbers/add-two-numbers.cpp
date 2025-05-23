/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
          
          ListNode* temp=new ListNode();
          ListNode* ans=temp;
        int carry=0,sum=0;
        while(l1!=NULL ||l2!=NULL ||carry)
        {
             if(l1!=NULL)
             {
                 sum+=l1->val;
                 l1=l1->next;
             }
             if(l2!=NULL)
             {
                 sum+=l2->val;
                 l2=l2->next;
             }
             sum+=carry;
             ListNode* newnode= new ListNode(sum%10);
             carry=sum/10,sum=0;
            temp->next=newnode;
            temp=temp->next;
        }
        return ans->next;
    }
};