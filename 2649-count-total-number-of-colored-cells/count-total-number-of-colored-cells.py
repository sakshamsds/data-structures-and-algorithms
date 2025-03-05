'''
    1   1 * 4
    5   2 * 4
    13  3 * 4
'''

class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1
        for i in range(n):
            res += i * 4
        return res