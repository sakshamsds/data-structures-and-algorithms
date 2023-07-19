from typing import List
import heapq

# https://leetcode.com/problems/sort-array-by-increasing-frequency/solutions/2904426/heap/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # make freq map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # store (freq, key) pairs in heap
        heap = []
        for key in freq_map:
            heapq.heappush(heap, (freq_map[key], -key))     # use -key for the requirement

        # pop smallest freq and store in new list
        res = []
        while heap:
            freq, key = heapq.heappop(heap)
            res += [-key] * freq

        return res

print(Solution().frequencySort([1,1,2,2,2,3]))


        
