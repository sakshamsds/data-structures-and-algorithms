# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(-1, head)
        cur = dummy

        beforeLeft = None
        for _ in range(left):
            beforeLeft = cur
            cur = cur.next
        leftNode = cur

        prev = None
        for _ in range(right - left + 1):
            nxt = cur.next         
            cur.next = prev
            prev = cur
            cur = nxt

        leftNode.next = cur
        beforeLeft.next = prev
        return dummy.next        