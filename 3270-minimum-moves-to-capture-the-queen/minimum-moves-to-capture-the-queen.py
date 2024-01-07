class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # either 1 or 2
        # rook movement
        if a == e:  # queen in same row
            if a == c and (d - b) * (d - f) < 0:    # bishop between q and r
                return 2
            else:
                return 1
        elif b == f:
            if b == d and (c - a) * (c - e) < 0:    # bishop between q and r
                return 2
            else:
                return 1
        # bishop movement
        elif c - e == d - f:    # \ diagonal
            if a - e == b - f and (a - c) * (a - e) < 0:
                return 2
            else:
                return 1
        elif c - e == f - d:    # / diagonal
            if a - e == f - b and (a - c) * (a - e) < 0:
                return 2
            else:
                return 1
        return 2        # worst case