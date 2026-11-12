# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(-1, head)

        cur = dummy
        for _ in range(n + 1):
            cur = cur.next

        prev = dummy
        while cur:
            prev = prev.next
            cur = cur.next

        prev.next = prev.next.next
        return dummy.next