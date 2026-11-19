class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s)
        freqs = [(-freq, char) for char, freq in counts.items()]
        heapq.heapify(freqs)

        N = len(s)
        if -freqs[0][0] > (N + 1) // 2:
            return ""

        res = [''] * N
        i = 0
        while freqs:
            freq, char = heapq.heappop(freqs)
            freq = -freq
            for _ in range(freq):
                res[i] = char
                i += 2
                if i >= len(s):
                    i = 1

        return ''.join(res)