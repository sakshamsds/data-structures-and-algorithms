# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(start):
            if not start:
                return None

            # last group
            cur = start
            for _ in range(k):
                if not cur:
                    return start
                cur = cur.next

            prev = None
            cur = start
            # nxt = cur.next
            for _ in range(k):
                if not cur:
                    break
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            start.next = reverse(nxt)
            return prev
            
        return reverse(head)
