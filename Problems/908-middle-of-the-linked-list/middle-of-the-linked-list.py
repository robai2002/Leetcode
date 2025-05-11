# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow = head
        while slow and slow.next:
            slow = slow.next
            if slow:slow = slow.next
            head = head.next
        return head

