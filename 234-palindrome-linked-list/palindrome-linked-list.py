# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow.val)       # mid = slow
        
        # reverse after mid
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        # while head:
            # print(head.val)
            # head = head.next
        
        while prev:
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        
        return True