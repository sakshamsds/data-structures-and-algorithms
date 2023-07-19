# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry goes to the next node

        cur = head = ListNode(0, None)
        carry = 0 

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next

        return head.next

        #     if l1 and l2:
        #         sum = l1.val + l2.val + carry
        #         carry = sum // 10
        #         cur.next = ListNode(sum % 10)
        #         l1 = l1.next
        #         l2 = l2.next
        #     elif l1:
        #         sum = l1.val + carry
        #         carry = sum // 10
        #         cur.next = ListNode(sum % 10)
        #         l1 = l1.next
        #     else:
        #         sum = l2.val + carry
        #         carry = sum // 10
        #         cur.next = ListNode(sum % 10)
        #         l2 = l2.next
        #     cur = cur.next

        # if carry != 0:
        #     cur.next = ListNode(carry)

        # return head.next

# Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
# Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(9))), ListNode(5, ListNode(6, ListNode(4, ListNode(9)))))