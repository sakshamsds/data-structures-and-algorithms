# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# a1, a2, c1, c2, c3, None, b1, b2, b3, c1
# b1, b2, b3, c1, c2, c3, None, a1, a2, c1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA, curB = headA, headB
        
        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA