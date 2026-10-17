'''
-
    ---------
        ---------
            ---
                    -----
'''


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x : (x[0], x[1]))

        res = [[-1, -1]]

        # if prev overlaps with current, update prev
        # if not, add current to the res

        for start, end in intervals:
            prev_start, prev_end = res[-1][0], res[-1][1]

            if start <= prev_end:   # overlap
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])

        return res[1:]
