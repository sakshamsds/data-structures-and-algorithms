# https://leetcode.com/problems/merge-nodes-in-between-zeros/
# 2181. Merge Nodes in Between Zeros

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        new_head = dummy
        current = head.next
        # keep summing up until we find a zero
        sum = 0
        while current:
            sum += current.val
            if current.val == 0:
                dummy.next = ListNode(sum, None)
                dummy = dummy.next
                sum = 0
            current = current.next
        return new_head.next
