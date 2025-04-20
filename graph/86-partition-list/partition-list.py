# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        left,right = ListNode(),ListNode
        left_curr,right_curr = left,right
        while head:
            if head.val<x:
                left_curr.next = head
                left_curr = head
            else:
                right_curr.next = head
                right_curr = head
            head = head.next
        right_curr.next = None
        left_curr.next = right.next
        return left.next