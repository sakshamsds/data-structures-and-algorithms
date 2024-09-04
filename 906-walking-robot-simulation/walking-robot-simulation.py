class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # find distance from orgin after every move
        obs = set()
        for ox, oy in obstacles:
            obs.add((ox, oy))

        d = 'N'     # ['N', 'W', 'S', 'E']
        x, y = 0, 0
        mx_dist = 0

        for cmd in commands:
            if d == 'N':
                if cmd == -2:
                    d = 'W'
                elif cmd == -1:
                    d = 'E'
                else:
                    k = 1
                    while k <= cmd and (x, y + k) not in obs:
                        k += 1
                    y += k - 1
            elif d == 'W':
                if cmd == -2:
                    d = 'S'
                elif cmd == -1:
                    d = 'N'
                else:
                    k = 1
                    while k <= cmd and (x - k, y) not in obs:
                        k += 1
                    x -= k - 1
            elif d == 'S':
                if cmd == -2:
                    d = 'E'
                elif cmd == -1:
                    d = 'W'
                else:
                    k = 1
                    while k <= cmd and (x, y - k) not in obs:
                        k += 1
                    y -= k - 1
            elif d == 'E':
                if cmd == -2:
                    d = 'N'
                elif cmd == -1:
                    d = 'S'
                else:
                    k = 1
                    while k <= cmd and (x + k, y) not in obs:
                        k += 1
                    x += k - 1
            mx_dist = max(mx_dist, x ** 2 + y ** 2)

        return mx_dist