class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        idx_map = {}  # map char -> last idx
        start_idx = 0
        max_size = 0  

        for i, c in enumerate(s):
            if c not in idx_map and len(idx_map) == 2:
                min_idx = min(idx_map.values())
                del_key = next(key for key, value in idx_map.items() if value == min_idx)
                del idx_map[del_key]
                start_idx = min_idx + 1

            idx_map[c] = i
            max_size = max(max_size, i - start_idx + 1)

        return max_size