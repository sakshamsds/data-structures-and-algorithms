class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = collections.defaultdict(int)
        longest = 0
        l = 0
        max_freq = 0
        for r, c in enumerate(s):
            freq_map[c] += 1
            max_freq = max(max_freq, freq_map[c])

            # how many swapping used in the window
            while (r - l + 1) - max_freq > k:
                freq_map[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest