class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = len(s) - ones
        return (ones - 1) * '1' + zeros * '0' + '1' 