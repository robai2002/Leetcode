# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        def marge(x,y):
            head = ListNode(0)
            cur = head
            while x and y:
                if x.val<y.val:
                    cur.next = x
                    x = x.next
                else:
                    cur.next = y
                    y = y.next
                cur =cur .next
            if x:
                cur.next = x
            if y:
                cur.next = y
            return head.next



        def marge_sort(low: int,high: int):
            if low>high:
                return None
            if low == high:
                return lists[low]
            mid = (high+low)//2
            x = marge_sort(low,mid)
            y = marge_sort(mid+1,high)
            return marge(x,y)

        return marge_sort(0,n-1)
            