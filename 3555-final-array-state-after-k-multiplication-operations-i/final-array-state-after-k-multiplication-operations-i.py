class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        min_heap = []
        for i, num in enumerate(nums):  # n * logn
            heapq.heappush(min_heap, (num, i))

        for _ in range(k):      # k * logn
            num, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (num * multiplier, i))

        res = [0] * len(nums)
        for num, i in min_heap:
            res[i] = num

        return res 

        