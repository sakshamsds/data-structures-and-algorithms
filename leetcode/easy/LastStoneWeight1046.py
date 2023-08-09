import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
            
        while len(stones) >= 2:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if x == y:
                pass
            else:
                new_stone = y - x
                heapq.heappush(stones, -new_stone)

        return 0 if len(stones) == 0 else -stones[0]