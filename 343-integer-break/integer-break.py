class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        num3, rem = divmod(n, 3)        # divide by 3
        if rem == 0:
            return 3 ** num3
        elif rem == 1:
            return 3 ** (num3 - 1) * 4
        else:
            return 3 ** num3 * 2