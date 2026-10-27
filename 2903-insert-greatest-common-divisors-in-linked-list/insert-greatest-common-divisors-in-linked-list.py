# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = head, head.next

        def gcd(a, b):
            if a % b == 0:
                return b
            return gcd(b, a % b)


        while cur:
            larger, smaller = max(prev.val, cur.val), min(prev.val, cur.val)
            prev.next = ListNode(val=gcd(larger, smaller), next=cur)
            prev = cur
            cur = cur.next

        return head
