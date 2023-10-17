# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1, head)
        ptr1 = dummy
        ptr2 = dummy
        
        for _ in range(n + 1):
            ptr2 = ptr2.next
            
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        # print(ptr1.val)
        ptr1.next = ptr1.next.next
        
        return dummy.next