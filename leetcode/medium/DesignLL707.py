# https://leetcode.com/problems/design-linked-list/
# 707. Design Linked List
# https://www.youtube.com/watch?v=Wf4QhpdVFQo

class Node:
    def __init__(self, val, next) -> None:
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
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(val, itr.next)
                break
            itr = itr.next
            count+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def print(self) -> None:
        itr = self.head
        while itr:
            print(itr.val, sep=None)
        
if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(2)
    obj.print()
    
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
# [[],                 [2],          [1],        [2],        [7],        [3],        [2],        [5],       [5],        [5],        [6],       [4]]