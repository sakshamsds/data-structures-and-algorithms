'''

0 1    -> dummy
0 1   -> 1
0 1 1     -> 2
0 1 2 1       -> 4
0 1 3 3 1         -> 8
0 1 4 6 4 1           -> 16

total = 2 ^ (k - 1)

'''

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured] # flow

        for row  in range(1, query_row + 1):
            cur_row = [0] * (row + 1)
            print(prev_row)
            for i in range(row):
                extra = prev_row[i] - 1
                if extra > 0:
                    cur_row[i] += 0.5 * extra
                    cur_row[i + 1] += 0.5 * extra
            prev_row = cur_row

        # print(prev_row)

        return min(1, prev_row[query_glass])