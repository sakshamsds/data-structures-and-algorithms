"""
    possible solutions, 101, 010
"""

class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros_left, ones_left = 0, 0
        zeros_right, ones_right = s.count("0"), s.count("1")

        total = 0
        for digit in s:
            if digit == "0":
                zeros_right -= 1
                zeros_left += 1
                total += ones_left * ones_right
            else:
                ones_right -= 1
                ones_left += 1
                total += zeros_left * zeros_right
        return total