class Solution:
    def reorganizeString(self, s: str) -> str:
        most_common, highest_freq = s[0], 0
        freqs = collections.defaultdict(int)
        for c in s:
            freqs[c] += 1
            if freqs[c] > highest_freq:
                most_common = c
                highest_freq += 1

        if highest_freq > ceil(len(s) / 2):
            return ""

        res = [""] * len(s)
        i = 0
        for _ in range(highest_freq):
            res[i] = most_common
            i += 2

        freqs.pop(most_common)
        for c, freq in freqs.items():
            for _ in range(freq):
                if i >= len(s):
                    i = 1
                res[i] = c
                i += 2

        return ''.join(res)
        