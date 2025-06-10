class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = collections.Counter(s)

        max_odd, min_even = 0, 101
        for _, f in freqs.items():
            if f & 1 == 1:
                max_odd = max(max_odd, f)
            else:
                min_even = min(min_even, f)

        # min_even = 0 if min_even == 101 else min_even
        return max_odd - min_even