class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        idx_map = {}
        start_idx, max_size = 0, 1
        
        for i, c in enumerate(s):
            if c not in idx_map and len(idx_map) == k:
                min_idx = min(idx_map.values())
                del_key = next(key for key, value in idx_map.items() if value == min_idx)
                del idx_map[del_key]
                start_idx = min_idx + 1

            idx_map[c] = i
            max_size = max(max_size, i - start_idx + 1)
        
        return max_size