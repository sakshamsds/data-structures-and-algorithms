'''
char -> freq mapping
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = collections.Counter(s)

        mx_heap = []
        for c, freq in freqs.items():
            heapq.heappush(mx_heap, (-freq, c))

        res = []
        while mx_heap:
            freq, c = heapq.heappop(mx_heap)
            res.extend([c] * -freq)
        
        return ''.join(res)
