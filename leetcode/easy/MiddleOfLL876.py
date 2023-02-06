# https://leetcode.com/problems/middle-of-the-linked-list/
# 876. Middle of the Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow and fast node concept

        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow


ll_head = ListNode(1)
ll_2 = ListNode(2)
ll_3 = ListNode(3)
ll_4 = ListNode(4)
ll_5 = ListNode(5)
ll_head.next = ll_2
ll_2.next = ll_3
ll_3.next = ll_4
ll_4.next = ll_5

sol = Solution()
print(sol.middleNode(ll_head).val)

ll_6 = ListNode(6)
ll_5.next = ll_6
print(sol.middleNode(ll_head).val)
