# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, nxt = head, head.next

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        while prev and nxt:
            mn, mx = min(prev.val, nxt.val), max(prev.val, nxt.val)
            prev.next = ListNode(gcd(mx, mn), nxt)
            prev = nxt
            nxt = nxt.next

        return head