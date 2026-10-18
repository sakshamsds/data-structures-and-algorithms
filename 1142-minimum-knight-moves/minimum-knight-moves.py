class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [
            (1, 2), (2, 1),
            (-1, 2), (-2, 1),
            (-1, -2), (-2, -1),
            (1, -2), (2, -1),
        ]

        q = deque([(0, 0)])
        visited = set()
        moves = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == x and c == y:
                    return moves

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in visited:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))   
            moves += 1

        return -1