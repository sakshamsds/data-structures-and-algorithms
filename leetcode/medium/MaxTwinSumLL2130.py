# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# 2130. Maximum Twin Sum of a Linked List
# https://www.youtube.com/watch?v=doj95MelfSA

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # get to the middle of the linked list and reverse the second half

        # get the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow
        # reverse the second half
        prev = None
        while current:
            tmp = current
            current = current.next
            tmp.next = prev
            prev = tmp

        end = prev
        start = head

        max_twin_sum = -1
        while end:
            max_twin_sum = max(max_twin_sum, start.val + end.val)
            end = end.next
            start = start.next

        return max_twin_sum