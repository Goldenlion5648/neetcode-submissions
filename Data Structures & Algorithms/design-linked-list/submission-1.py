class Node:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        pos = 0
        cur = self.head
        if index >= self.size:
            return -1
        while pos < index:
            pos += 1
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        new_head = Node(val, self.head)
        self.head = new_head
        if not self.tail:
            self.tail = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return
        else:
            pos = 0
            prev = None
            cur = self.head
            while pos < index:
                pos += 1
                prev = cur
                cur = cur.next
            prev.next = Node(val, cur)
            self.size += 1
            

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        pos = 0
        prev = None
        cur = self.head
        while pos < index:
            pos += 1
            prev = cur
            cur = cur.next 
        prev.next = cur.next
        if index == self.size - 1:
            self.tail = prev
        
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)