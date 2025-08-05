class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # bfs

        # nbrs +a, -b
        # cannot jump backwards twice
        # sanity check, cannot be negative
        # start = 0

        # target = x

        q = collections.deque([(0, False)])
        forbidden = set(forbidden)
        visited = set((0, False))       # number, last_backward
        min_jumps = 0

        while q:
            num_nbrs = len(q)
            for _ in range(num_nbrs):
                cur, last_backward = q.popleft()
                if cur == x:
                    return min_jumps

                nbrs = [(cur + a, False)]
                if not last_backward:
                    nbrs.append((cur - b, True))

                for nbr, is_backward in nbrs[::-1]:
                    if (
                        nbr < 0 or
                        nbr > 2000 + a + b or
                        (nbr, is_backward) in visited or
                        nbr in forbidden
                    ):
                        continue
                    q.append((nbr, is_backward))
                    visited.add((nbr, is_backward))
            min_jumps += 1

        return -1
