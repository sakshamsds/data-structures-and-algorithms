'''
1 + 1 * 4 + 2 * 4 + 3 * 4
1 + 4 * (n * (n - 1)) / 2
'''

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)