'''
    .   L   .   R   .   .   .   L   R   .   .   L   .   .
                    1R  2R  3R          1R  2R          
    1L              3L  2L  1L          2L  1L
    L   L   .   R   R   .   L   L   R   R   L   L   .   .
    LL.RR.LLRRLL..
'''

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        solved = list(dominoes)

        # solve for R
        time = 0
        for i, c in enumerate(solved):
            if c == 'L':
                time = 0
            elif c == 'R':
                time = 1
            elif time > 0:
                solved[i] = time
                time += 1

        # print(solved)

        # solve for L
        time = 0
        for i in range(len(solved) - 1, -1, -1):
            c = solved[i]
            if c == 'R':
                time = 0
            elif c == 'L':
                time = 1
            else:
                if time == 0:
                    if c != '.':
                        solved[i] = 'R'
                else:
                    if c == '.' or c > time:
                        solved[i] = 'L'
                    elif time == c:
                        solved[i] = '.'
                    else:
                        solved[i] = 'R'
                    time += 1

        # print(solved)

        return ''.join(solved)