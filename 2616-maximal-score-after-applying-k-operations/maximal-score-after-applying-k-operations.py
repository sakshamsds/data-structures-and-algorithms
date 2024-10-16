class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        mx_heap = [-num for num in nums]
        heapq.heapify(mx_heap)

        score = 0
        for _ in range(k):
            largest = -heapq.heappop(mx_heap)
            score += largest
            heapq.heappush(mx_heap, -math.ceil(largest / 3))

        return score