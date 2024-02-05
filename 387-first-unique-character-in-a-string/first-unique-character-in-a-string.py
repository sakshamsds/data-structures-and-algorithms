class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqs = Counter(s)
        for i, c in enumerate(s):
            if freqs[c] == 1:
                return i
        return -1