# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next

        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp

        left, right = head, prev
        while right and left:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True
    