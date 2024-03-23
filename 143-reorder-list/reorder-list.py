# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None or head.next.next is None:
            return head

        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # print(slow.val)
        prev = None
        mid = slow.next
        slow.next = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp

        p1, p2 = head, prev
        dummy = ListNode(-1)
        cur = dummy
        while p1 and p2:
            cur.next = p1
            p1 = p1.next
            cur = cur.next
            cur.next = p2
            p2 = p2.next
            cur = cur.next

        return dummy.next
