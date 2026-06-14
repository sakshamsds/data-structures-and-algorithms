# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        cur = slow
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        left, right = head, prev
        maxTwinSum = 0
        while right:
            maxTwinSum = max(maxTwinSum, left.val + right.val)
            left = left.next
            right = right.next

        return maxTwinSum