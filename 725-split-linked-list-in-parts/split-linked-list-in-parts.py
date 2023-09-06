# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1

        # print(length)
        res = []
        cur = head
        while length > 0:
            # print(length)
            # numbers to add 
            split = []
            split_size = math.ceil(length / k)
            cur_head = cur
            prev = cur
            for _ in range(split_size):
                # split.append(cur.val)
                prev = cur
                cur = cur.next
            prev.next = None
            res.append(cur_head)
            length -= split_size
            k -= 1

        while k > 0:
            res.append(None)
            k -= 1

        # for row in res:
            # print(row)
        return res