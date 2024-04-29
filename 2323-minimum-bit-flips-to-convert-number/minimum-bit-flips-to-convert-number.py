class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # find different bits using XOR operation
        xor = start ^ goal
        ones = 0
        while xor > 0:
            xor = xor & (xor - 1)
            ones += 1
        return ones