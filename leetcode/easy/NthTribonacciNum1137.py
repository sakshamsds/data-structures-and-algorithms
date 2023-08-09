class Solution:
    def tribonacci(self, n: int) -> int:
        zero, one, two = 0, 1, 1
        for _ in range(n):
            zero, one, two = one, two, zero + one + two

        return zero