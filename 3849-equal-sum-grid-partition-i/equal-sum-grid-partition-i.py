class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        for row in grid:
            total += sum(row)

        cur = 0
        for row in grid:
            cur += sum(row)
            if cur * 2 == total:
                return True
            if cur * 2 > total:
                break
        
        cur = 0
        for c in range(len(grid[0])):
            for r in range(len(grid)):
                cur += grid[r][c]
            if cur * 2 == total:
                return True
            if cur * 2 > total:
                break        

        return False