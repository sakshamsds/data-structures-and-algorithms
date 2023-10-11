class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_map = collections.defaultdict(int)
        
        for c1, c2 in zip(s, t):
            freq_map[c1] += 1
            freq_map[c2] -= 1
            
        for _, v in freq_map.items():
            if v != 0:
                return False
            
        return True