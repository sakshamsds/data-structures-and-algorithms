class Solution:
    def reorganizeString(self, s: str) -> str:
        most_common_char, most_common_freq = None, 0
        freqs = collections.defaultdict(int)
        for c in s:
            freqs[c] += 1
            if freqs[c] > most_common_freq:
                most_common_freq = freqs[c]
                most_common_char = c

        if most_common_freq > math.ceil(len(s) / 2):
            return ""

        res = [''] * len(s)
        for i in range(most_common_freq):
            res[2 * i] = most_common_char

        i = i * 2 + 2
        freqs.pop(most_common_char)
        for c, freq in freqs.items():
            for _ in range(freq):
                if i >= len(s):
                    i = 1
                res[i] = c
                i += 2

        return ''.join(res)

