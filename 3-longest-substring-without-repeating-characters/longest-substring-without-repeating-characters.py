'''
    a   b   c   a   b   c   b   b
    l           r
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx_map = dict()
        l = 0
        longest = 0

        for r, c in enumerate(s):
            if c in last_idx_map and last_idx_map[c] >= l:
                l = last_idx_map[c] + 1
            longest = max(longest, r - l + 1)
            last_idx_map[c] = r

        return longest