class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        half_sum = nums_sum / 2
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        num_ops = 0

        while nums_sum > half_sum:
            num_ops += 1
            largest = -heapq.heappop(max_heap)
            nums_sum -= largest / 2
            heapq.heappush(max_heap, -largest / 2)

        return num_ops


