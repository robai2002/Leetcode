# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans
        nums = set(nums)
        while head:
            if head.val not in nums:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return ans.next