"""
numbers greater than 999 has one comma, n > 999,999 has two and so on
"""

class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        for i in range(1, 6):
            res += max(0, n - (1000 ** i - 1))
        return res
        