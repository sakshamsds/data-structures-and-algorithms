# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            cur = node
            prev = None
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        cur = reverse(head)
        carry = 0
        reversed_head = cur
        while cur:
            twice = cur.val * 2 + carry
            carry = twice // 10
            cur.val = twice % 10
            if cur.next is None:        # reached the last node
                if carry != 0:
                    cur.next = ListNode(carry)
                break
            cur = cur.next

        y = reverse(reversed_head)
        # x = y
        # while x:
        #     print(x.val, end='-> ')
        #     x = x.next
        return y
            

Solution().doubleIt(ListNode(9, ListNode(9, ListNode(9))))
# Solution().doubleIt(ListNode(1, ListNode(8, ListNode(9))))