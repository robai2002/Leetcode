# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def marge_list(l: int,h: int) ->Optional[ListNode]:
            if l > h:
                return None
            if l ==h:
                return lists[h]
            mid = (l+h)//2
            l1,l2 = marge_list(l,mid),marge_list(mid+1,h)
            ans = ListNode()
            curr = ans 
            while l1 and l2:
                if l1.val<l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
             
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            return ans.next

        
        return marge_list(0,len(lists)-1)