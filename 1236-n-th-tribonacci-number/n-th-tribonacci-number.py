class Solution:
    def tribonacci(self, n: int) -> int:
        prev, cur, nxt = 0, 1, 1

        for _ in range(n):
            prev, cur, nxt = cur, nxt, prev + cur + nxt

        return prev

