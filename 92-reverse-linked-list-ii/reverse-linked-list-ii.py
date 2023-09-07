# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        left_prev, cur = dummy, head

        # reach node at position left
        for _ in range(left - 1):
            left_prev, cur = left_prev.next, cur.next

        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next