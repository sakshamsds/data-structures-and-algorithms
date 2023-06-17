# https://leetcode.com/problems/rotate-list/
# 61. Rotate List

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        size = 1
        current = head
        while current.next:
            size += 1
            current = current.next

        # print("size: ", size)

        k = k%size
        if k == 0:
            return head
        
        # print(current.val)

        current.next = head
        for _ in range(0, size-k):
            current = current.next

        # print(current.val)

        head = current.next
        current.next = None
        return head
    

if __name__ == "__main__":
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    head = ListNode(0, ListNode(1, ListNode(2, None)))

    obj = Solution()
    new_head = obj.rotateRight(head, 4)

    while new_head:
        print(new_head.val, end="->")
        new_head = new_head.next
