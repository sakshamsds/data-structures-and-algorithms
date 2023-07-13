import collections
import heapq
from typing import List

class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        print(collections.Counter(arr))
        heap = list(collections.Counter(arr).values())
        heapq.heapify(heap)
        while k>0:
            k -= heapq.heappop(heap)

        return len(heap) + 1 if k < 0 else len(heap)
        # return len(heap) + (k < 0)

    # def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

    #     # make the frequency map
    #     freq_map = {}
    #     for key in arr:
    #         if key in freq_map:
    #             freq_map[key] += 1
    #         else:
    #             freq_map[key] = 1

    #     # sort python dict
    #     freq_map = dict(sorted(freq_map.items(), key=lambda x:x[1], reverse=False))

    #     # print(freq_map)
    #     unique_elements = len(freq_map)
    #     removals = 0
    #     # remove the most distinct elements
    #     for key in freq_map:
    #         if k <= 0 or freq_map[key] > k:
    #             break

    #         if freq_map[key] <= k:
    #             removals += 1
    #             k -= freq_map[key]
                
    #     return unique_elements - removals
    
print(Solution().findLeastNumOfUniqueInts([5,5,4], 1))
print(Solution().findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))