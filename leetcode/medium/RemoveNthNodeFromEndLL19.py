# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # maintain two pointers and delay one with n steps
        fast = head
        slow = head

        while n>0:
            fast = fast.next
            n-=1
        
        # if n = length of the list, remove first element
        if fast is None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head



# test

def iterate_LL(head):
    while head is not None:
        print(head.val)
        head = head.next
    return


ll_head = ListNode(1)

sol = Solution()
iterate_LL(sol.removeNthFromEnd(ll_head, 1))

ll_2 = ListNode(2)
ll_3 = ListNode(3)
ll_4 = ListNode(4)
ll_5 = ListNode(5)
ll_head.next = ll_2
ll_2.next = ll_3
ll_3.next = ll_4
ll_4.next = ll_5

iterate_LL(sol.removeNthFromEnd(ll_head, 2))
# iterate_LL(sol.removeNthFromEnd(ll_head, 5))

