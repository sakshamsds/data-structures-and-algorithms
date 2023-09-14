class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx_map = collections.defaultdict(list)
        
        for i, c in enumerate(s):
            idx_map[c].append(i)
                
        # print(idx_map)    # ordered
        for k, v in idx_map.items():
            if len(v) == 1:
                return v[0]
        
        return -1
        