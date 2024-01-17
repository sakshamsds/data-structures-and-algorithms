class Solution:
    def minTimeToType(self, word: str) -> int:
        time, prev = len(word), 'a'
        for c in word:
            diff = abs(ord(c) - ord(prev))
            time += min(diff, 26 - diff)
            prev = c
        return time