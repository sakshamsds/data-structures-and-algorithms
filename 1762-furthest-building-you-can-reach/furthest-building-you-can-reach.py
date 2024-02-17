class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff < 0:
                continue
            heapq.heappush(min_heap, diff)
            if len(min_heap) > ladders:     # use bricks for smaller heights
                min_diff = heapq.heappop(min_heap)
                if min_diff > bricks:
                    return i - 1
                bricks -= min_diff
            # print(bricks)
        return len(heights) - 1     # reached the last index