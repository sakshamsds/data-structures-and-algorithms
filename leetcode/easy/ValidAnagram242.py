class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map = dict()
        for i in range(len(s)):
            freq_map[s[i]] = freq_map.get(s[i], 0) + 1
            freq_map[t[i]] = freq_map.get(t[i], 0) - 1

        # print(freq_map)
        for _, value in freq_map.items():
            if value != 0:
                return False
        
        return True