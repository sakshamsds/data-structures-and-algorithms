class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {
            1 : 'LR',
            2 : 'UD',
            3 : 'LD',
            4 : 'RD',
            5 : 'LU',
            6 : 'RU',
        }

        prevNextMap = {
            'L' : 'R',
            'R' : 'L',
            'U' : 'D',
            'D' : 'U'
        }

        ROWS, COLS = len(grid), len(grid[0])



        def isValid(enter):
            visited = set()
            r, c = 0, 0
            while 0 <= r < ROWS and 0 <= c < COLS and enter in directions[grid[r][c]] and (r, c) not in visited:
                visited.add((r, c))     
                # print(r, c)
                if (r, c) == (ROWS - 1, COLS - 1):
                    return True
                nxt = [d for d in directions[grid[r][c]] if d != enter][0]
                if nxt == 'R':
                    c += 1
                elif nxt == 'L':
                    c -= 1
                elif nxt == 'U':
                    r -= 1
                else:   # nxt = 'D'
                    r += 1
                enter = prevNextMap[nxt]
            return False

        return isValid('L') or isValid('R') or isValid('U') or isValid('D')