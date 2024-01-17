class Solution:
    def minTimeToType(self, word: str) -> int:
        time, prev = 0, 'a'
        for c in word:
            diff = abs(ord(c) - ord(prev))
            time += min(diff, 26 - diff) + 1
            prev = c
        return time