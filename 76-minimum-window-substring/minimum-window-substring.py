'''
A - 1, B - 1, C - 1

A   D   O   B   E   C   O   D   E   B   A   N   C
                                    l   r
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict, window_dict = collections.Counter(t), defaultdict(int)
        l, r = 0, 0
        minL, minR = 0, len(s)
        min_size = float('inf')

        def match():
            for c, freq in t_dict.items():
                if window_dict[c] < freq:
                    return False
            return True

        for r in range(len(s)):
            window_dict[s[r]] += 1

            if not match():
                continue        # continue moving the r pointer

            # if match, shift until no match
            while match() and l <= r:
                if min_size > r - l + 1:
                    min_size = r - l + 1
                    minL, minR = l, r
                window_dict[s[l]] -= 1
                l += 1

        return "" if min_size == float('inf') else s[minL:minR + 1]
