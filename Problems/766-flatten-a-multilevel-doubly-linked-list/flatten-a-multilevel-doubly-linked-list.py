"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return head
        l = [head]
        curr = Node(1,None,None,None)
        while l:
            x = l[-1]
            l.pop()
            if x.next:l.append(x.next)
            if x.child:l.append(x.child)
            x.child = None
            x.next = None
            x.prev = curr
            curr.next = x
            curr = x
        head.prev = None
        return head
