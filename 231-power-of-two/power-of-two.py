class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ones = 0
        while n > 0:
            n = n & (n - 1)
            ones += 1
        return ones == 1