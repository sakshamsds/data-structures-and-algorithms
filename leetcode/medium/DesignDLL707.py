# https://leetcode.com/problems/design-linked-list/
# 707. Design Linked List
# https://www.youtube.com/watch?v=Wf4QhpdVFQo

class Node:
    def __init__(self, prev, val, next) -> None:
        self.prev = prev
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count=0
        itr = self.head
        while itr:
            if count == index:
                return itr.val
            itr = itr.next  
            count+=1    
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(None, val, self.head)
        self.head = new_node
        if self.head != None:
            self.head.prev = new_node

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(None, val, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        new_node = Node(itr, val, None)
        itr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Node(itr, val, itr.next)
                itr.next = new_node
                itr.next.prev = new_node
                break
            itr = itr.next
            count+=1
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1 and itr.next != None and itr.next.next != None:
                itr.next = itr.next.next
                itr.next.next.prev = itr
                break
            itr = itr.next
            count+=1

    def print(self) -> None:
        itr = self.head
        while itr:
            print(itr.val, end=" <-> ")
            itr = itr.next
        
# if __name__ == '__main__':
#     obj = MyLinkedList()
#     obj.addAtHead(2)
#     obj.deleteAtIndex(1)
#     obj.addAtHead(2)
#     obj.addAtHead(7)
#     obj.addAtHead(3)
#     obj.addAtHead(2)
#     obj.addAtHead(5)
#     obj.addAtTail(5)
#     print(obj.get(5))
#     obj.deleteAtIndex(6)
#     obj.deleteAtIndex(4)
#     obj.print()

    # obj.addAtTail(3)
    # obj.addAtIndex(1, 2)
    # print(obj.get(1))
    # print(obj.get(1))
    

# Your MyLinkedList object will be instantiated and called as such:
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
# [[],                 [2],          [1],        [2],        [7],        [3],        [2],        [5],       [5],        [5],        [6],       [4]]