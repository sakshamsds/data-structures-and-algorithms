class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            for dr, dc in [(1, 0), (0, 1)]:  # go down or right only
                nr, nc = r + dr, c + dc
                if (
                    nr < 0 or nr >= rows or
                    nc < 0 or nc >= cols or
                    board[nr][nc] == '.' or
                    (nr, nc) in visited
                ):
                    continue
                dfs(nr, nc)

        num_ships = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X' and (r, c) not in visited:
                    dfs(r, c)
                    num_ships += 1

        return num_ships

        

        
