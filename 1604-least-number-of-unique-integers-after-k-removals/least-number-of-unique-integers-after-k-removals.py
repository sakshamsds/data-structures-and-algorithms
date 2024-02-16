'''
num -> freq pairs
5 - 2
4 - 1
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        min_heap = []
        freqs = collections.Counter(arr)
        for num, freq in freqs.items():
            min_heap.append((freq, num))
        heapq.heapify(min_heap)
        while k >= 0 and min_heap:
            freq, _ = heapq.heappop(min_heap)
            if k < freq:
                return len(min_heap) + 1
            k -= freq
        return 0