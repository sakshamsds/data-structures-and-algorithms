# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        dummy = ListNode(-1, head)
        prev, cur = dummy, head
        while cur:
            if cur.val in nums:
                cur = cur.next
                continue
            
            prev.next = cur
            prev = cur
            cur = cur.next
        prev.next = None

        return dummy.next
        