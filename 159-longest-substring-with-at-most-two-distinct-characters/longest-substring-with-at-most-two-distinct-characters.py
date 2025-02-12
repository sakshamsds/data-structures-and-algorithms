class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        idx_map = {}        # map char -> last idx
        start_idx, max_size = 0, 1

        for i, c in enumerate(s):
            if c not in idx_map and len(idx_map) == 2:
                # find smallest idx and remove the key value pair corresponding to that
                del_key, min_idx = None, i
                for k, v in idx_map.items():
                    if v < min_idx:
                        del_key, min_idx = k, v
                # idx_map.delete(del_key)
                del idx_map[del_key]
                start_idx = min_idx + 1

            idx_map[c] = i
            max_size = max(max_size, i - start_idx + 1)
    
        return max_size
            