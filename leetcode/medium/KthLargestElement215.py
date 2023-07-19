import heapq
from typing import List

#heapify in O(n)
# https://leetcode.com/problems/kth-largest-element-in-an-array/editorial/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # build min heap of size k
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)     # pop the smallest element if size > k

        return heap[0]      # return the kth largest element


        # build max heap
        # heap = [-x for x in nums]
        # heapq.heapify(heap)

        # # pop k-1 times from max heap
        # for _ in range(k - 1):
        #     heapq.heappop(heap)

        # return -heapq.heappop(heap)
        

print(Solution().findKthLargest([3,2,1,5,6,4], 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))