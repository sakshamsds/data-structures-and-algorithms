# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # go to the middle of the list
        # reverse it
        # merge alternatively

        dummy = ListNode(-1, head)
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None

        # reverse
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        p2 = prev
        p1 = dummy.next

        i = 0
        while p1 and p2:
            if i % 2 == 0:
                tmp = p1.next
                p1.next = p2
                p1 = tmp
            else:
                tmp = p2.next
                p2.next = p1
                p2 = tmp
            i += 1
        
        return dummy.next