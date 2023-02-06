# https://leetcode.com/problems/intersection-of-two-linked-lists/
# 160. Intersection of Two Linked Lists
# https://www.youtube.com/watch?v=D0X0BONOQhI

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # Solution 1
        # calculate length of a 
        # calculate length of b
        # iterate the bigger list by the difference of distance
        # iterate both lists and find the common element

        # Solution 2
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1

        # # altogether different problem
        # # to check if there is any intersection
        # # iterate both the list,
        # # the last node should be same for intersection
        # currentA = headA
        # currentB = headB
        # while currentA.next is not None:
        #     currentA = currentA.next
        # while currentB.next is not None:
        #     currentB = currentB.next
        # return currentA == currentB

        # # brute force - Time Limit Exceeded
        # brute force two - , save list one in hashset

        # new_headA = ListNode(-1)
        # new_headA.next = headA
        # new_headB = ListNode(-2)
        # new_headB.next = headB
        # currentA = new_headA
        # if headA == headB:
        #     return headA
        # while currentA is not None:
        #     currentB = new_headB
        #     print(currentA)
        #     while currentB is not None:
        #         if currentA.next == currentB.next:
        #             if currentA.next is None and currentB.next is None:
        #                 if currentA == currentB:
        #                     return currentA
        #             else:
        #                 return currentA.next
        #         currentB = currentB.next
        #     currentA = currentA.next
        # return None