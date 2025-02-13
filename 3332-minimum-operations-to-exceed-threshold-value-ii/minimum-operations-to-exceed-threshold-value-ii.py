class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0

        while len(nums) >= 2:
            min1 = heapq.heappop(nums)
            if min1 >= k:
                return ops

            ops += 1
            min2 = heapq.heappop(nums)
            heapq.heappush(nums, min1 * 2 + min2)

        return ops