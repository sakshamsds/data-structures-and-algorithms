'''
    1               4
        2                           8
            3               6

    -----------------
        -----------
            ---------------------
'''

class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for left, right in intervals[1:]:
            prev_left, prev_right = res[-1]
            if prev_left < left and prev_right < right:
                res.append((left, right))

        return len(res)

