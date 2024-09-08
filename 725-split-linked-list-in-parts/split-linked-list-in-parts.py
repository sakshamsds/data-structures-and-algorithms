# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        def getSize(head):
            cur = head
            size = 0
            while cur:
                cur = cur.next
                size += 1
            return size

        rem_size = getSize(head)
        # print(size)

        def getPart(head, size):
            cur = head
            for _ in range(size - 1):
                cur = cur.next
            next_head = cur.next
            cur.next = None
            return head, next_head


        res = []
        next_head = head
        while k > 0:
            part_size = math.ceil(rem_size / k)
            if part_size == 0:
                res.extend([None for _ in range(k)])
                break
            part_head, next_head = getPart(next_head, part_size)
            res.append(part_head)
            rem_size -= part_size
            k -= 1

        return res


