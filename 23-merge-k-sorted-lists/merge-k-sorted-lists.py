# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Write comparator for heap node
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))

        dummy = ListNode(-1)
        cur = dummy
        while heap:
            min_node = heapq.heappop(heap).node
            cur.next = min_node
            if min_node.next:
                heapq.heappush(heap, HeapNode(min_node.next))
            cur = min_node

        return dummy.next

