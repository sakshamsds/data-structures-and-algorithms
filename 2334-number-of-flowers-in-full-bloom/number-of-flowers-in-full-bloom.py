class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort(key = lambda x : x)

        min_heap = []       # sort by end values
        res = {}
        i = 0
        for p in sorted(people):
            # add flowers which can be seen
            while i < len(flowers) and flowers[i][0] <= p:
                heapq.heappush(min_heap, (flowers[i][1]))
                i += 1

            # remove flowers which cannot be seen
            while min_heap and min_heap[0] < p:
                heapq.heappop(min_heap)

            res[p] = len(min_heap)

        return [res[p] for p in people]

        
            