class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, d, mx = 0, 0, 0, 0

        for c in commands:
            if c == -2:
                d = (d - 1) % 4
            elif c == -1:
                d = (d + 1) % 4
            else:
                dx, dy = directions[d]
                while c and (x + dx, y + dy) not in obstacles:
                    x += dx
                    y += dy
                    c -= 1
                mx = max(mx, x ** 2 + y **2)
        return mx
