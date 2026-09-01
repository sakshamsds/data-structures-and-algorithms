# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first, second, third = head, head.next, head.next.next

        minD, maxD = 10**5, 0
        firstIdx = -1
        prevIdx = -1

        idx = 0
        while third:    # calculate
            # print(first.val, second.val, third.val)
            if (second.val < first.val and second.val < third.val) or \
                (second.val > first.val and second.val > third.val):
                # critical point
                # print(idx)
                if firstIdx == -1:
                    firstIdx = idx
                else:
                    minD = min(minD, idx - prevIdx)
                    maxD = idx - firstIdx
                prevIdx = idx

            idx += 1
            first, second, third = first.next, second.next, third.next

        if maxD == 0:
            return [-1, -1]

        return [minD, maxD]

                