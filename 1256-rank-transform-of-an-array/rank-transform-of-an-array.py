class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        heap = []
        for num in arr:
            heapq.heappush(heap, num)

        # make rank list in a hashmap
        rank_map = dict()
        rank = 1
        prev = float('inf')
        while heap:
            num = heapq.heappop(heap)
            if num not in rank_map:
                rank_map[num] = rank
                if num != prev:
                    rank += 1
                prev = num

        res = []
        for num in arr:
            rank = rank_map[num]
            res.append(rank)

        return res        