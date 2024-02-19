class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        one_bits = 0
        while n > 0:
            if n % 2 == 1:
                one_bits += 1
            if one_bits > 1:
                return False
            n = n >> 1
        return True