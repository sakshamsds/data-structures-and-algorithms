# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def getGCD(l, s):
            if s == 0:
                return l
            return getGCD(s, l%s)

        prev = head
        cur = head.next

        while cur:
            s = min(prev.val, cur.val)
            l = max(prev.val, cur.val)
            prev.next = ListNode(getGCD(l, s), cur)
            prev = cur
            cur = cur.next

        return head

        
