class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = collections.Counter(s)
        mx_heap = []        # most common word
        for char, freq in freqs.items():
            mx_heap.append((-freq, char))
        heapq.heapify(mx_heap)

        res = []
        while mx_heap:
            f1, c1 = heapq.heappop(mx_heap)

            if not mx_heap:
                if f1 == -1:
                    res.append(c1)
                    break
                else:
                    return ""

            f2, c2 = heapq.heappop(mx_heap)

            res.append(c1)
            res.append(c2)

            f1 += 1
            f2 += 1
            if f1 < 0:
                heapq.heappush(mx_heap, (f1, c1))
            if f2 < 0:
                heapq.heappush(mx_heap, (f2, c2))

        return ''.join(res)
                        

