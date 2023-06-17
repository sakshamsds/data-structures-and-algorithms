# https://leetcode.com/problems/swap-nodes-in-pairs/
# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head
        
        # new_head = head.next
        # current = head

        # def swap(current):
        #     if not current:
        #         return None
            
        #     if current.next:
        #         # swap
        #         next = current.next
        #         current.next = swap(current.next.next)
        #         next.next = current
        #         return next
        #     else:
        #         return current
            
        # swap(current)
        # return new_head

        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            next_pair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = next_pair
            prev.next = second

            # update ptrs
            prev = curr
            curr = next_pair
        
        return dummy.next
    

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, None)))
    output = Solution().swapPairs(head)
    while output:
        print(output.val, end="->")
        output = output.next