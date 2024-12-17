class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = collections.Counter(s)

        max_heap = []
        for letter, freq in count.items():
            heapq.heappush(max_heap, (-ord(letter), letter, freq))

        res = []
        while max_heap:
            _, letter, freq = heapq.heappop(max_heap)
            if freq <= repeatLimit:
                res.append(letter * freq)
            else:
                res.append(letter * repeatLimit)
                if not max_heap:
                    break
                _, letter2, freq2 = heapq.heappop(max_heap)
                res.append(letter2)
                heapq.heappush(max_heap, (-ord(letter), letter, freq - repeatLimit))
                if freq2 > 1:
                    heapq.heappush(max_heap, (-ord(letter2), letter2, freq2 - 1))

        return ''.join(res)