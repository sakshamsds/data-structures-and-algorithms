class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        max_heap = [(-freq, c) for c, freq in counter.items()]
        heapq.heapify(max_heap)

        res = []
        while max_heap:
            f1, c1 = heapq.heappop(max_heap)
            res.append(c1)

            if not max_heap:        # no other element is left
                return ''.join(res) if f1 == -1 else ""

            f2, c2 = heapq.heappop(max_heap)
            res.append(c2)

            if f1 < -1: heapq.heappush(max_heap, (f1 + 1, c1))
            if f2 < -1: heapq.heappush(max_heap, (f2 + 1, c2))            

        return ''.join(res)