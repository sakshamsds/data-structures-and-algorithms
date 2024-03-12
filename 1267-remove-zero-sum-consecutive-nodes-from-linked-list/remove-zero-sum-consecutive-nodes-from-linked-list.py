# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1   2   -2  3   1

1   3   1   4   5
    2   0   3   4
        -2  -1  0
            3   4
                1
'''

class Solution:
    def removeZeroSumSublists(self, head):
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next
    # def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # convert to array
    #     nums = []
    #     while head:
    #         nums.append(head.val)
    #         head = head.next
    #     # print(nums)
    #     # remove element where subarray sum == 0
    #     for 


    #     # convert to linkedlist
    #     dummy = ListNode(-1)
    #     cur = dummy
    #     for num in nums:
    #         cur.next = ListNode(num)
    #         cur = cur.next

    #     return dummy.next