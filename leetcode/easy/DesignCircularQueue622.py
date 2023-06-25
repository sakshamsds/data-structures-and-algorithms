
# array implementation, two pointers, front and rear
# linkedlist implementation

class ListNode:
    def __init__(self, prev:None, val, next:None):
        self.prev = prev
        self.val = val
        self.next = next

# left --------------> <------------------- right, left and right are our dummy nodes

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = ListNode(None, -1, None)
        self.right = ListNode(self.left, -1, None)
        self.left.next = self.right
        self.k = k
        self.size = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        new_node = ListNode(self.right.prev, value, self.right)
        self.right.prev.next = new_node
        self.right.prev = new_node
        self.size += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()