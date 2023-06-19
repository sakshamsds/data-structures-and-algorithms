# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# 1721. Swapping Nodes in a Linked List
# https://www.youtube.com/watch?v=4LsrgMyQIjQ

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # two pointers faster solution
        right, left = head, head

        for _ in range(k-1):
            left = left.next

        current = left
        while current.next:
            right, current = right.next, current.next

        temp = left.val
        left.val = right.val
        right.val = temp

        return head
    
        # current = head
        # size = 1
        # while current:
        #     current = current.next
        #     size+=1

        # left = head
        # for _ in range(k-1):
        #     left = left.next

        # right = head
        # for _ in range(size-k-1):
        #     right = right.next
        
        # temp = left.val
        # left.val = right.val
        # right.val = temp
        # return head