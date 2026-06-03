class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.length = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return -1
        prev, curr = self.head, self.head.next
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = Node(val, curr)
        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return -1
        prev, curr = self.head, self.head.next
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)