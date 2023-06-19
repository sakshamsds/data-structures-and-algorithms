# https://leetcode.com/problems/palindrome-linked-list/
# 234. Palindrome Linked List

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # # array solution
        # nums = []
        # while head:
        #     nums.append(head.val)
        #     head = head.next
        # l, r = 0, len(nums)-1
        # while l<r:
        #     if nums[l] != nums[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True


        # fast and slow pointers, reach the end and middle of the list

        fast = head
        slow = head

        # get to the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # start reversing from the middle
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True
    

if __name__ == "__main__":
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1, None)))))
    output = Solution().isPalindrome(ll)
    print(output)


