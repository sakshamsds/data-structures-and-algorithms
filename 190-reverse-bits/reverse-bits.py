class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(31):
            digit = n & 1 if n > 0 else 0
            res += digit
            res = res << 1
            n = n >> 1
        return res