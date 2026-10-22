class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or   
                (r, c) in visited or
                board[r][c] != word[i]
            ):
                return False

            visited.add((r, c))

            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True
            
            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False