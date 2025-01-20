class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        nbr_directions = [
            (1, 1), (1, 0), (1, -1),
            (0, 1), (0, -1),
            (-1, 1), (-1, 0), (-1, -1)
        ]

        # calculate nbrs for alive cells
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    for dr, dc in nbr_directions:
                        nr, nc = r + dr, c + dc
                        if (
                            nr < 0 or nr >= rows or
                            nc < 0 or nc >= cols 
                        ):
                            continue
                        board[r][c] += 1 if board[nr][nc] > 0 else 0
                    board[r][c] *= 2

        # calculate for dead cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 0:
                    cnt = 0
                    for dr, dc in nbr_directions:
                        nr, nc = r + dr, c + dc
                        if (
                            nr < 0 or nr >= rows or
                            nc < 0 or nc >= cols 
                        ):
                            continue
                        cnt += 1 if board[nr][nc] > 1 else 0
                    if cnt == 3:
                        board[r][c] = 1

        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 1:
                    board[r][c] = 1 if (board[r][c] // 2) in [3, 4] else 0
