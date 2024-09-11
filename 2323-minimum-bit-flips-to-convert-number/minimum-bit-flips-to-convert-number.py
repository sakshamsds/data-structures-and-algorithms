class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal
        res = 0
        while n > 0:
            n = n & (n - 1)
            res += 1
        return res