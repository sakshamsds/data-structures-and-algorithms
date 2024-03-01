class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        store = collections.defaultdict(int)
        for r in range(n):
            store[tuple(grid[r])] += 1
        res = 0
        for c in range(n):
            col = []
            for r in range(n):
                col.append(grid[r][c])
            res += store[tuple(col)]
        return res