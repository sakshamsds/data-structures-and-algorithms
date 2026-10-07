class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap -> (freq, num)

        freqs = collections.Counter(nums)
        min_heap = []
        for num, freq in freqs.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for _, num in min_heap]