class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        moves = [0] * rows

        for c in range(cols - 2, -1, -1):
            newMoves = [0] * len(moves)
            for r in range(rows):
                # topRight
                if r > 0 and grid[r][c] < grid[r - 1][c + 1]:
                    newMoves[r] = max(newMoves[r], 1 + moves[r - 1])

                # right
                if grid[r][c] < grid[r][c + 1]:
                    newMoves[r] = max(newMoves[r], 1 + moves[r])

                # bottomRight
                if r < rows - 1 and grid[r][c] < grid[r + 1][c + 1]:
                    newMoves[r] = max(newMoves[r], 1 + moves[r + 1])

            moves = newMoves
            # print(moves)
        
        return max(moves)
