class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        freqs = [0] * 26

        for c in s:
            freqs[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_freqs = [0] * 26
            for i in range(25):
                new_freqs[i + 1] = freqs[i]

            new_freqs[0] += freqs[-1]
            new_freqs[1] += freqs[-1]

            freqs = new_freqs

        return sum(freqs) % (10 ** 9 + 7)

            