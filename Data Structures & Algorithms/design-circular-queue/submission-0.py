class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node(-math.inf)
        self.end = self.head
        self.cap = k
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.len == 0:
            self.head = new_node
            self.end = self.head
        else:
            self.end.next = new_node
            self.end = self.end.next
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.len == 0:
            return False
        self.head = self.head.next
        self.len -= 1
        return True

    def Front(self) -> int:
        if self.len == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.len == 0:
            return -1
        return self.end.val
        

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()