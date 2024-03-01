class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        store = collections.defaultdict(int)
        for row in grid:
            store[tuple(row)] += 1
        res = 0
        for col in zip(*grid):
            res += store[tuple(col)]
        return res