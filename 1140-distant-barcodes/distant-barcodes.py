'''
1 - 4
2 - 2
3 - 2

1   2   1   2   1   3   1   3   
0   1   2   3   4   5   6   7   
                    l
'''


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        max_heap = []
        freqs = Counter(barcodes)
        for bc, freq in freqs.items():
            heapq.heappush(max_heap, (-freq, bc))

        res = [0] * len(barcodes)
        even_i, odd_i = 0, 1        # fill even indices first then odd indices
        while max_heap:
            freq, bc = heapq.heappop(max_heap)
            for f in range(-freq):
                if even_i < len(barcodes):
                    res[even_i] = bc
                    even_i += 2
                else:
                    res[odd_i] = bc
                    odd_i += 2
            # print('res', res)
        # print(res)
        return res
