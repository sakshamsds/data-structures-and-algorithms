class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # heap -> element, idx

        minHeap = []
        for i, num in enumerate(arr):
            heapq.heappush(minHeap, (num, i))

        prev, rank = float(-inf), 0
        while minHeap:
            num, i = heapq.heappop(minHeap)
            if num > prev:
                rank += 1
            arr[i] = rank
            prev = num

        return arr