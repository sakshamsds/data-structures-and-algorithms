'''
    1           4
            3               6
        2                           8
'''

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        # print(intervals)
        result = 0
        lastEnd = 0

        # check if the current is gonna get consumed or not
        for _, end in intervals:
            if lastEnd < end:
                result += 1
                lastEnd = end

        return result


