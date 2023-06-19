# https://leetcode.com/problems/reverse-linked-list-ii/
# 92. Reverse Linked List II

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # USING DUMMY NODE
        dummy = ListNode(-1, head)
        left_prev, current = dummy, head

        # 1) reach node at position "left"
        for _ in range(left-1):
            left_prev, current = current, current.next

        # Now current="left", left_prev = "node before left"
        # 2) reverse from left to right
        prev = None
        for _ in range(right-left+1):
            temp = current
            current = current.next
            temp.next = prev
            prev = temp

        # 3) update pointers
        left_prev.next.next = current
        left_prev.next = prev

        return dummy.next

        # if head is None or head.next is None or left == right:
        #     return head
        
        # current = head
        # before_left = None
        # count_left = left
        # while count_left>1:
        #     count_left -= 1
        #     before_left = current
        #     current = current.next

        # left_ptr = current
        # prev = left_ptr
        # current = current.next

        # # print(before_left.val)
        # # print(left_ptr.val)

        # count_right = right-left
        # while count_right>0:
        #     count_right-=1
        #     temp = current
        #     current = current.next
        #     temp.next = prev
        #     prev = temp

        # right_ptr = prev
        # if left != 1:
        #     before_left.next = right_ptr
        # else:
        #     head = right_ptr
        # left_ptr.next = current

        # # print(right_ptr.val)
        # # print(current.val)
        # return head
    

if __name__ == "__main__":
    # ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
    # head = Solution().reverseBetween(ll, 2, 5)
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    head = Solution().reverseBetween(ll, 1, 4)
    # ll = ListNode(5, None)
    # head = Solution().reverseBetween(ll, 1, 1)
    # ll = ListNode(3, ListNode(5, None))
    # head = Solution().reverseBetween(ll, 1, 1)
    while head:
        print(head.val, end="->")
        head = head.next